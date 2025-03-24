from time import sleep
import tkinter as tk
import subprocess
import threading
from tkinter import messagebox
import json
#import 開啟OLLAMAA

# 初始化 Tkinter 主視窗
root = tk.Tk()
root.withdraw()  # 隱藏主視窗，因為我們只需要 Toplevel 視窗

# 全局變數：保存當前選擇的模型
選定模型 = tk.StringVar()
選定模型.set("尚未選擇模型")  # 預設值

def 模型設定():
    # 建立新的 Toplevel 視窗
    模型設定視窗 = tk.Toplevel()
    模型設定視窗.title("模型設定")
    模型設定視窗.geometry("600x400")
    模型設定視窗.iconbitmap("1.ico")
    模型設定視窗.resizable(True, True)

    # 建立 Frame
    frame4 = tk.Frame(模型設定視窗, bg="#3C3C3C")
    frame4.pack(expand=True, fill="both")
    frame5 = tk.Frame(模型設定視窗, bg="#3C3C3C")
    frame5.pack(expand=True, fill="both")
    frame6 = tk.Frame(模型設定視窗, bg="#3C3C3C")
    frame6.pack(expand=True, fill="both")

    try:
        # 讀取 MODS.json
        with open('MODS.json', 'r', encoding='utf-8') as file:
            mods_data = json.load(file)

        模型選項 = [mod['name'] for mod in mods_data]
        選項變數 = tk.StringVar(value="請先選擇模型")

        def 顯示參數(*args):
            當前模型 = 選項變數.get()
            參數框.config(state=tk.NORMAL)
            參數框.delete("1.0", tk.END)

            if 當前模型 == "請先選擇模型":
                參數框.insert(tk.END, "請先選擇模型")
            else:
                for mod in mods_data:
                    if mod['name'] == 當前模型:
                        參數文字 = "\n".join([f"{key}: {value}" for key, value in mod['parameters'].items()])
                        參數框.insert(tk.END, 參數文字)
                        break

            參數框.config(state=tk.DISABLED)

        選項變數.trace_add("write", 顯示參數)

        # 下拉選單
        下載選單 = tk.OptionMenu(frame4, 選項變數, *模型選項)
        下載選單.pack(fill="both", pady=10, padx=10)

        # 參數顯示框
        參數框 = tk.Text(frame5, wrap="word", height=2, borderwidth=1, state=tk.DISABLED)
        參數框.pack(pady=10, padx=10, fill="both", expand=True)

        def 使用此模型():
            def 模型操作():
                global 選定模型  # 引用全域變數
                #開啟OLLAMA.開啟_ollama()
                sleep(1.5)
                當前模型 = 選項變數.get()
                選定模型.set(當前模型)  # 更新全域變數

                if 當前模型 == "請先選擇模型":
                    messagebox.showerror("錯誤", "請先選擇模型")
                    return

                try:
                    with open('MODS.json', 'r', encoding='utf-8') as file:
                        模組下載 = json.load(file)
                except Exception as e:
                    messagebox.showerror("錯誤", f"讀取 MODS.json 時發生錯誤: {e}")
                    return

                模組 = next((mod for mod in 模組下載 if mod['name'] == 當前模型), None)
                if not 模組:
                    messagebox.showerror("錯誤", "找不到選定的模型")
                    return

                try:
                    result = subprocess.run(["ollama", "list"], capture_output=True, text=True)
                    installed_models = [line.split()[0] for line in result.stdout.splitlines()]
                    sleep(1.5)  # 等待 0.5 秒
                except Exception as e:
                    messagebox.showerror("錯誤", f"檢查已安裝模型時發生錯誤: {e}")
                    return

                if 當前模型 not in installed_models:
                    if not messagebox.askyesno("下載模型", f"模型 {當前模型} 尚未安裝，是否下載？"):
                        return

                    def 下載模型():
                        try:
                            subprocess.run(["ollama", "pull", 當前模型], check=True)
                            messagebox.showinfo("成功", f"模型 {當前模型} 下載完成")
                            subprocess.Popen(f"ollama run {當前模型}", shell=True)
                            模型設定視窗.destroy()  # 成功後關閉模型設定視窗
                        except Exception as e:
                            messagebox.showerror("錯誤", f"下載模型時發生錯誤: {e}")

                    threading.Thread(target=下載模型, daemon=True).start()
                else:
                    try:
                        subprocess.Popen(f"ollama run {當前模型}", shell=True)
                        messagebox.showinfo("成功", f"已成功啟動模型: {當前模型}")
                        模型設定視窗.destroy()  # 成功後關閉模型設定視窗
                    except Exception as e:
                        messagebox.showerror("錯誤", f"啟動模型時發生錯誤: {e}")

            threading.Thread(target=模型操作, daemon=True).start()

        # 使用模型按鈕
        use_model_btn = tk.Button(frame6, text="使用模型", command=使用此模型)
        use_model_btn.pack(pady=10, padx=10)
        
        # 其它輸入框
        自己輸入 = tk.Entry(frame6)
        自己輸入.pack(fill="both", pady=10, padx=10)

        other_input_btn = tk.Button(frame6, text="其它自己輸入")
        other_input_btn.pack(pady=10, padx=10)
        
    except FileNotFoundError:
        messagebox.showerror("錯誤", "請檢查檔案完整性\"選項---->檢查\"")
        模型設定視窗.destroy()

    模型設定視窗.mainloop()

def 檢查():
    選定模型.get()
    print("當前選擇的模型:", 選定模型.get())

# 測試用主視窗
if __name__ == "__main__":
    root = tk.Tk()
    root.title("主視窗")
    root.geometry("400x300")

    # 按鈕：打開模型設定視窗
    btn_open_model_setting = tk.Button(root, text="模型設定", command=模型設定)
    btn_open_model_setting.pack(pady=20)

    # 按鈕：檢查當前選擇的模型
    btn_check_model = tk.Button(root, text="檢查模型", command=檢查)
    btn_check_model.pack(pady=20)

    print(選定模型.get())
    sleep(0.5)

    root.mainloop()