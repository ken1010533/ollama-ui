# 宣告使用的函式庫
import tkinter as tk
import ctypes
import subprocess
import threading
import tkinter.ttk as ttk
from tkinter import messagebox
import json

import tqdm
#######################################################################################################

# 创建窗口
root = tk.Tk()                             # 创建主窗口
root.title("功能丰富的 GUI 应用")           # 設定視窗標題
window_width = root.winfo_screenwidth()    # 取得螢幕寬度
window_height = root.winfo_screenheight()  # 取得螢幕高度
width = 600
height = 500
left = int((window_width - width)/2)       # 計算左上 x 座標
top = int((window_height - height)/2)      # 計算左上 y 座標
root.geometry(f'{width}x{height}+{left}+{top}')   # 設定視窗大小與位置
root.geometry("600x500")                   # 設定視窗大小
root.iconbitmap("1.ico")                   # 設定視窗圖示
root.resizable(True, True)                 # 設定視窗寬高可變動
ctypes.windll.kernel32.FreeConsole()      # 隱藏命令提示字元視窗
frame3 = tk.Frame(root) # 創建 Frame
frame3.pack(side="bottom", fill="both") # 將 Frame 放置在視窗
frame1 = tk.Frame(root) # 創建 Frame
frame1.pack(side='bottom', fill="both") # 將 Frame 放置在視窗
frame2 = tk.Frame(root) # 創建 Frame
frame2.pack(side='top', fill="both") # 將 Frame 放置在視窗
frame4 = None # 創建 Frame 4 用來放置模型設定視窗

#######################################################################################################



#######################################################################################################
        #輸入框

default_text = "輸入任何問題吧..."  # 提示文字
def 顏色(): 
    current_theme = root.tk.call("ttk::style", "theme", "use" )     
    if current_theme == "clam":
         text.config(bg="white", fg="black", insertbackground="black")  
    else:
         text.config(bg="#3C3C3C", fg="white", insertbackground="white")  

def on_text_focus_in(event):
    text.config(fg="black", insertbackground="black")  # 變成正常輸入顏色
    if text.get("1.0", tk.END).strip() == default_text:
        text.delete("1.0", tk.END)  # 清除內容

def on_text_focus_out(event):
    if not text.get("1.0", tk.END).strip():  # 如果輸入框是空的
        text.insert("1.0", default_text)  # 插入提示文字
        text.config(fg="gray", insertbackground="gray")  # 變淡
        顏色()
# 創建 Text 元件（wrap="word" 讓文字自動換行）
text = tk.Text(frame1, wrap="word", height=1, relief="ridge", borderwidth=3) # 創建 Text
text.grid(column=3, row=2, sticky="nsew", pady=10)  # 讓 Text 填滿 Frame

text.insert("1.0", default_text)  # 插入提示文字
text.config(fg="gray", insertbackground="gray")  #   初始顏色變淡
text.bind("<FocusIn>", on_text_focus_in)  # 當點擊輸入框時
text.bind("<FocusOut>", on_text_focus_out)  # 當離開輸入框時

scrollbar = tk.Scrollbar(frame1, command=text.yview)  # 創建 Scrollbar
text.config(yscrollcommand=scrollbar.set) # 讓 Text 與 Scrollbar 連動
frame1.grid_rowconfigure(2, weight=1) # 設定第 2 列的高度可變動
frame1.grid_columnconfigure(3, weight=1) #  設定第 3 欄的寬度可變動

# 綁定事件來調整 Text 的高度
def adjust_text_height(event):
    lines = int(text.index('end-1c').split('.')[0])
    new_height = min(max(lines, 1), 10)  # 確保高度至少為 1 且最多為 10
    text.config(height=new_height)
    if lines > 4:
        scrollbar.grid(column=4, row=2, sticky="ns")
    else:
        scrollbar.grid_remove()

text.bind('<KeyRelease>', adjust_text_height)

#######################################################################################################

    # 輸出文字框
output_text = tk.Text(frame2, wrap="word", height=206, relief="ridge", borderwidth=3)
output_text.grid(column=3, row=2, sticky="nsew", padx=10, pady=10)
output_text.config(state=tk.DISABLED)  # 設定為只讀模式

scrollbar_output = tk.Scrollbar(frame2, command=output_text.yview)
output_text.config(yscrollcommand=scrollbar_output.set)
frame2.grid_rowconfigure(2, weight=1)
frame2.grid_columnconfigure(3, weight=1)
scrollbar_output.grid(column=4, row=2, sticky="ns")

# 使用多線程來更新輸出文字框
output_thread = threading.Thread( daemon=True)
output_thread.start()
#######################################################################################################

    #畫布功能

畫布功能=tk.Button(frame3,text="畫布功能")
畫布功能.grid(column=5, row=5)
#######################################################################################################

#模型功能設定
def 模型設定():
    # 建立新的 Toplevel 視窗0

    模型設定視窗 = tk.Toplevel()
    模型設定視窗.title("模型設定")
    模型設定視窗.geometry("600x400")
    模型設定視窗.iconbitmap("1.ico")
    模型設定視窗.resizable(True, True)

    global frame4  
    frame4 = tk.Frame(模型設定視窗,bg="#3C3C3C")
    frame4.config(bg="#3C3C3C")
    frame4.pack(expand=True, fill="both", anchor="center",)


    try:
        # 讀取 MODS.json 文件
        with open('MODS.json', 'r', encoding='utf-8') as file:
            mods_data = json.load(file)

        # 選項變數 & 下拉選單
        模型選項 = [mod['name'] for mod in mods_data ]
        選項變數 = tk.StringVar(value="請先選擇模型")

        def 顯示參數(*args):
            選定模型 = 選項變數.get()
            if 選定模型 == "請先選擇模型":
                參數框.config(state=tk.NORMAL)
                參數框.delete("1.0", tk.END)
                參數框.insert(tk.END, "請先選擇模型")
                參數框.config(state=tk.DISABLED)
            else:
                for mod in mods_data:
                    if mod['name'] == 選定模型:
                        參數 = mod['parameters']
                        參數文字 = "\n".join([f"{key}: {value}" for key, value in 參數.items()])
                        參數框.config(state=tk.NORMAL)
                        參數框.delete("1.0", tk.END)
                        參數框.insert(tk.END, 參數文字)
                        參數框.config(state=tk.DISABLED)
                        break

        選項變數.trace_add("write", 顯示參數)

        下載選單 = tk.OptionMenu(frame4,選項變數, *模型選項)
        下載選單.pack(fill="both", pady=10, padx=10)

        # 顯示參數的文字框
        參數框 = tk.Text(frame4, wrap="word", height=1, borderwidth=1, state=tk.DISABLED, bg="#3C3C3C", fg="white")
        參數框.pack( pady=1, padx=1, fill="both", expand=True, anchor="center")
    





































        def 使用此模型():
            選定模型 = 選項變數.get()

            # 檢查是否選擇了模型
            if 選定模型 == "請先選擇模型":
                messagebox.showerror("錯誤", "請先選擇模型")
                return  # 提前退出，避免後續錯誤處理
            
            # 嘗試讀取 MODS.json
            try:
                with open('MODS.json', 'r', encoding='utf-8') as file:
                    模組下載 = json.load(file)
            except Exception as e:
                messagebox.showerror("錯誤", f"讀取 MODS.json 時發生錯誤: {e}")
                return

            # 查找選定的模型
            模組 = next((mod for mod in 模組下載 if mod['name'] == 選定模型), None)
            
            if not 模組:
                messagebox.showerror("錯誤", "找不到選定的模型")
                return

            # 使用 ollama list 檢查是否已安裝模型
            try:
                result = subprocess.run(["ollama", "list"], capture_output=True, text=True)
                installed_models = [line.split()[0] for line in result.stdout.splitlines()]  # 提取模型名稱
            except Exception as e:
                messagebox.showerror("錯誤", f"檢查已安裝模型時發生錯誤: {e}")
                return

            if 選定模型 not in installed_models:
                if not messagebox.askyesno("下載模型", f"模型 {選定模型} 尚未安裝，是否下載？"):
                    return

                # 建立下載視窗
                下載進度視窗 = tk.Toplevel()
                下載進度視窗.title("下載進度")
                下載進度視窗.geometry("400x100")
                下載進度視窗.resizable(False, False)

                進度條 = ttk.Progressbar(下載進度視窗, orient="horizontal", length=300, mode="determinate")
                進度條.pack(pady=20)

                進度標籤 = tk.Label(下載進度視窗, text="下載中...")
                進度標籤.pack()

                def 更新進度條(進度, 總大小):
                    百分比 = (進度 / 總大小) * 100
                    下載進度視窗.after(1, lambda: 進度條.config(value=百分比))
                    下載進度視窗.after(1, lambda: 進度標籤.config(text=f"下載中... {進度}/{總大小} bytes ({百分比:.2f}%)"))

                # 下載模型函式
                def 下載模型():
                    try:
                        cmd = ["ollama", "pull", 選定模型]
                        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

                        總大小 = 模組.get('size')  # 預設總大小為 1GB
                        進度 = 0

                        for line in process.stdout:
                            if "pulling" in line.lower(tqdm):
                                # 解析進度
                                parts = line.split()
                                if len(parts) >= 4:
                                    try:
                                        進度 = int(parts[3])
                                        更新進度條(進度, 總大小)
                                    except ValueError:
                                        pass

                        下載進度視窗.after(1, lambda: 下載進度視窗.destroy())
                        messagebox.showinfo("成功", f"模型 {選定模型} 下載完成")
                    except Exception as e:
                        下載進度視窗.after(1, lambda: 下載進度視窗.destroy())
                        messagebox.showerror("錯誤", f"下載模型時發生錯誤: {e}")

                threading.Thread(target=下載模型, daemon=True).start()  # 在子執行緒中執行下載

            else:
                # 如果模型已安裝，直接啟動
                啟動指令 = 模組.get('command')
                if not 啟動指令:
                    messagebox.showerror("錯誤", "選定的模型沒有啟動指令")
                    return

                try:
                    subprocess.Popen(啟動指令, shell=True)
                    messagebox.showinfo("成功", f"已成功啟動模型: {選定模型}")
                except Exception as e:
                    messagebox.showerror("錯誤", f"啟動模型時發生錯誤: {e}")



































































            
    # 按鈕
        use_model_btn = tk.Button(frame4, text="使用模型",command=使用此模型)
        use_model_btn.pack( pady=10, padx=10)









        下載模型= ["模型1", "模型2", "模型3", "模型4", "模型5"]
        option_var1= tk.StringVar(value=下載模型[0])

        下載模型= tk.OptionMenu(frame4, option_var1, *下載模型)
        下載模型.pack(fill="both", pady=10, padx=10)

        download_model_btn = tk.Button(frame4, text="下載模型")
        download_model_btn.pack( pady=10, padx=10)

        自己輸入=tk.Entry(frame4)
        自己輸入.pack(fill="both", pady=10, padx=10)

        other_input_btn = tk.Button(frame4, text="其它自己輸入")
        other_input_btn.pack( pady=10, padx=10)
        
    except FileNotFoundError:
        messagebox.showerror("錯誤", "請檢查檔案完整性\"選項---->檢查\"")

        模型設定視窗.destroy()
    
    # 讓新視窗獨立運行
    toggle_theme1()
    模型設定視窗.mainloop()


模型設定=tk.Button(frame3,text="模型設定",command=模型設定)
模型設定.grid(column=4, row=5)
#######################################################################################################
        # 菜單
def set1():
    pass
def set2():
    open_settings_window()



def set3():
    on_closing()

菜單=tk.Menu(root)  # 创建菜单
設定子菜單=tk.Menu(菜單,tearoff=0)  # 创建子菜单 
設定子菜單.add_command(label="設定",command=set2)
設定子菜單.add_command(label="離開",command=set3)
菜單.add_cascade(label="選項",menu=設定子菜單)  # 添加子菜单到菜单

def info1():
    try:
        # 假設這裡是檢查 ollama 是否安裝的邏輯
        result = subprocess.run(["ollama", "--version"], capture_output=True, text=True)
        messagebox.showinfo("檢查結果", f"ollama 已安裝，版本: {result.stdout}")
    except Exception as e:
        messagebox.showerror("錯誤", f"發生錯誤: {e}")
def info2():
    pass
def info3():
   
   pass

資訊子菜單=tk.Menu(菜單,tearoff=0)  # 创建子菜单
資訊子菜單.add_command(label="檢查",command=info1)  # 添加子菜单命令
資訊子菜單.add_command(label="更新",command=info2)
資訊子菜單.add_command(label="資訊",command=info3)
菜單.add_cascade(label="其他",menu=資訊子菜單)  # 添加子菜单到菜单
root.config(menu=菜單)  # 將菜单添加到窗口
#######################################################################################################

#設定按鈕

root.tk.call("ttk::style", "theme", "use", "alt")
frame1.config(bg="#3C3C3C")
frame2.config(bg="#3C3C3C")
frame3.config(bg="#3C3C3C")
text.config(bg="#3C3C3C", fg="white", insertbackground="white")
output_text.config(bg="#3C3C3C", fg="white")

def toggle():
    toggle_theme()
    toggle_theme1()

def toggle_theme():
    current_theme = root.tk.call("ttk::style", "theme", "use" )

    if current_theme == "clam":
        root.tk.call("ttk::style", "theme", "use", "alt")
        frame1.config(bg="#3C3C3C")
        frame2.config(bg="#3C3C3C")
        frame3.config(bg="#3C3C3C")
        text.config(bg="#3C3C3C", fg="white", insertbackground="white")
        output_text.config(bg="#3C3C3C", fg="white")
    else:
        root.tk.call("ttk::style", "theme", "use", "clam")
        frame1.config(bg="white")
        frame2.config(bg="white")
        frame3.config(bg="white")
        text.config(bg="white", fg="black", insertbackground="black")   
        output_text.config(bg="white", fg="black")
def toggle_theme1():  
    current_theme = root.tk.call("ttk::style", "theme", "use" )     
    if current_theme == "clam":
        if frame4 is not None and frame4.winfo_exists():
             frame4.config(bg="white")
    else:
        if frame4 is not None and frame4.winfo_exists():
            frame4.config(bg="#3C3C3C")

def switch_language():
    current_title = root.title()
    new_title = "功能丰富的 GUI 应用" if current_title == "Feature-rich GUI Application" else "Feature-rich GUI Application"
    
    root.title(new_title)

def open_settings_window():
    settings_window = tk.Toplevel(root)
    settings_window.title("設定")
    settings_window.geometry("400x300")

    frame = ttk.Frame(settings_window, padding=20)
    frame.pack(expand=True, fill="both")
    language_button = ttk.Button(frame, text="語言切換", command=switch_language)
    language_button.pack(pady=10, anchor="center", expand=True, fill="both", ipadx=10, ipady=10)
    theme_button = ttk.Button(frame, text="色彩切換", command=toggle)
    theme_button.pack(pady=10, anchor="center", expand=True, fill="both", ipadx=10, ipady=10)
    離開按鈕 = ttk.Button(frame, text="離開", command=settings_window.destroy)
    離開按鈕.pack(pady=10, anchor="center", expand=True, fill="both", ipadx=10, ipady=10)

def threaded_function(func):
    thread = threading.Thread(target=func, daemon=True)
    thread.start()

# 初始化 ttk 樣式
style = ttk.Style()

#######################################################################################################

    #關閉應用程式
def on_closing():
    subprocess.Popen('taskkill /IM "ollama.exe" /F', shell=True)
    subprocess.Popen('taskkill /IM "ollama app.exe" /F', shell=True)
    root.after(1000, root.destroy)  # 延遲 1 秒後關閉應用程式

root.protocol("WM_DELETE_WINDOW", on_closing)


#######################################################################################################
    # 窗口运行
root.mainloop()  

#######################################################################################################