import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import subprocess
import os
import threading
import time
import ctypes

# 隱藏 CMD 視窗
ctypes.windll.kernel32.FreeConsole()

def toggle_menu():
    if menu_frame.winfo_viewable():
        menu_frame.pack_forget()
    else:
        menu_frame.pack(side="left", fill="y")

# 創建主窗口
root = tk.Tk()
root.title("Ollama Chat Interface")
root.geometry("800x600")  # 設置窗體大小
def check_ollama_installation():
    try:
        result = subprocess.run(['where', 'ollama'], capture_output=True, text=True, creationflags=subprocess.CREATE_NO_WINDOW)
        if result.returncode == 0:
            pass  # Add your logic here if needed
        else:
            if messagebox.askyesno("檢查結果", "Ollama 未安裝。是否要安裝？"):
                install_ollama()
            else:
                root.destroy()
    except Exception as e:
        messagebox.showerror("錯誤", f"無法檢查 Ollama 安裝狀態: {e}")
        root.destroy()

def install_ollama():
    try:
        # 假設這是安裝 Ollama 的命令，請根據實際情況修改
        subprocess.run(['powershell', '-Command', 'Start-Process', 'https://ollama.com/download/OllamaSetup.exe', '-Wait'], check=True, creationflags=subprocess.CREATE_NO_WINDOW)
        # 等待用戶下載安裝檔
        while not os.path.exists(os.path.join(os.path.expanduser("~"), "Downloads", "OllamaSetup.exe")):
            time.sleep(1)
        
        # 偵測用戶下載資料夾位置
        user_downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
        setup_path = os.path.join(user_downloads_folder, "OllamaSetup.exe")
        
        # 檢查安裝檔是否存在
        if not os.path.exists(setup_path):
            messagebox.showerror("錯誤", f"無法找到安裝檔: {setup_path}")
            root.destroy()
            return
        
        subprocess.run(['powershell', '-Command', 'Start-Process', setup_path, '-Wait'], check=True, creationflags=subprocess.CREATE_NO_WINDOW)
        messagebox.showinfo("安裝結果", "Ollama 安裝成功。")
    except Exception as e:
        messagebox.showerror("錯誤", f"無法安裝 Ollama: {e}")
        root.destroy()

check_ollama_installation()

# 創建選單框架
menu_frame = tk.Frame(root, width=100, bg="lightgray")
menu_frame.pack(side="left", fill="y")

# 在選單框架中添加亮色/暗色模式按鈕
def toggle_theme():
    if root.tk.call("ttk::style", "theme", "use") == "clam":
        root.tk.call("ttk::style", "theme", "use", "alt")
        content_frame.config(bg="#3C3C3C")
        chat_area.config(bg="#3C3C3C", fg="white", insertbackground="white")
    else:
        root.tk.call("ttk::style", "theme", "use", "clam")
        content_frame.config(bg="white")
        chat_area.config(bg="white", fg="#3C3C3C", insertbackground="#3C3C3C")

# 預設為白色主題
root.tk.call("ttk::style", "theme", "use", "clam")

theme_button = tk.Button(menu_frame, text="亮色/暗色模式", command=toggle_theme)
theme_button.pack(pady=10)

# 添加其他按鈕
# 第2個按鈕的地方改成顯示可以安裝的模型的下拉選單
install_label = ttk.Label(menu_frame, text="可安裝模型:")
install_label.pack(pady=5)

install_combobox = ttk.Combobox(menu_frame, state="readonly")
install_combobox.pack(pady=5)

def get_available_models():
    # 模擬可安裝模型列表
    models = [
        "deepseek-r1:1.5b",
        "deepseek-r1:7b",
        "deepseek-r1:8b",
        "deepseek-r1:14b",
        "deepseek-r1:32b",
        "deepseek-r1:70b",
        "deepseek-r1:671b"
    ]
    return models

install_combobox['values'] = get_available_models()
        

# 第3個按鈕是安裝第2個選擇的模型
def install_model():
    selected_model = install_combobox.get()
    if not selected_model:
        messagebox.showerror("錯誤", "請先選擇一個模型。")
        return

    try:
        subprocess.run(['ollama', 'install', selected_model], check=True, creationflags=subprocess.CREATE_NO_WINDOW)
        messagebox.showinfo("成功", f"模型 {selected_model} 安裝成功。")
        models_combobox['values'] = get_installed_models()  # 更新已安裝模型列表
    except Exception as e:
        messagebox.showerror("錯誤", f"無法安裝模型: {e}")

install_button = tk.Button(menu_frame, text="安裝選擇的模型", command=install_model)
install_button.pack(pady=5)

# 第4個按鈕的地方改成顯示安裝的模型的下拉選單
installed_label = ttk.Label(menu_frame, text="已安裝模型:")
installed_label.pack(pady=5)

installed_combobox = ttk.Combobox(menu_frame, state="readonly")
installed_combobox.pack(pady=5)
def get_installed_models():
    try:
        result = subprocess.run(['ollama', 'list'], capture_output=True, text=True, creationflags=subprocess.CREATE_NO_WINDOW)
        models = result.stdout.strip().split('\n')
        models = [model.split()[0] for model in models if model]  # 解析名稱
        
        # 過濾掉不需要的選項（例如名為 "NAME" 的選項）
        filtered_models = [model for model in models if model != "NAME"]
        
        return filtered_models
    except Exception as e:
        messagebox.showerror("錯誤", f"無法獲取模型列表: {e}")
        return []

installed_combobox['values'] = get_installed_models()

# 第4個按鈕是使用第4個選擇的模型
def use_installed_model():
    selected_model = installed_combobox.get()
    if not selected_model:
        messagebox.showerror("錯誤", "請先選擇一個模型。")
        return

    try:
        result = subprocess.run(['ollama', 'run', selected_model], capture_output=True, text=True, creationflags=subprocess.CREATE_NO_WINDOW)
        output_window = tk.Toplevel(root)
        output_window.title(f"模型 {selected_model} 執行結果")
        output_text = scrolledtext.ScrolledText(output_window, wrap=tk.WORD)
        output_text.pack(fill=tk.BOTH, expand=True)
        output_text.insert(tk.END, result.stdout)
        output_text.configure(state='disabled')
    except Exception as e:
        messagebox.showerror("錯誤", f"無法運行模型: {e}")

# 第5個按鈕是刪除第4個選擇的模型
def delete_model():
    selected_model = installed_combobox.get()
    if not selected_model:
        messagebox.showerror("錯誤", "請先選擇一個模型。")
        return

    try:
        subprocess.run(['ollama', 'delete', selected_model], check=True, creationflags=subprocess.CREATE_NO_WINDOW)
        messagebox.showinfo("成功", f"模型 {selected_model} 刪除成功。")
        models_combobox['values'] = get_installed_models()  # 更新已安裝模型列表
        installed_combobox['values'] = get_installed_models()  # 更新已安裝模型列表
    except Exception as e:
        messagebox.showerror("錯誤", f"無法刪除模型: {e}")

delete_button = tk.Button(menu_frame, text="刪除選擇的模型", command=delete_model)
delete_button.pack(pady=5)

# 創建主內容框架
content_frame = tk.Frame(root, bg="white")
content_frame.pack(side="right", fill="both", expand=True)

# 模型選擇下拉選單
frame_top = ttk.Frame(content_frame)
frame_top.pack(pady=10, fill=tk.X)

# 創建選單按鈕
menu_button = tk.Button(frame_top, text="顯示/隱藏選單", command=toggle_menu)
menu_button.pack(side=tk.LEFT, fill=tk.Y, padx=8)

models_label = ttk.Label(frame_top, text="選擇模型:")
models_label.pack(side=tk.LEFT, fill=tk.X, padx=5)

models_combobox = ttk.Combobox(frame_top, state="readonly")
models_combobox.pack(side=tk.LEFT, fill=tk.X, expand=True)

use_model_button = ttk.Button(frame_top, text="使用此模組", command=lambda: threading.Thread(target=run_selected_model).start())
use_model_button.pack(side=tk.RIGHT, padx=5)

def run_selected_model():
    selected_model = models_combobox.get()
    if not selected_model:
        messagebox.showerror("錯誤", "請先選擇一個模型。")
        return

    try:
        subprocess.run(['ollama', 'run', selected_model], check=True, creationflags=subprocess.CREATE_NO_WINDOW)
    except Exception as e:
        messagebox.showerror("錯誤", f"無法運行模型: {e}")

# 聊天區
chat_area = scrolledtext.ScrolledText(content_frame, height=20)
chat_area.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
chat_area.configure(state='disabled')  # 防止手動編輯

# 輸入區域
frame_input = ttk.Frame(content_frame)
frame_input.pack(fill=tk.X, pady=5)

input_entry = ttk.Entry(frame_input)
input_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, pady=5, ipadx=5)

def on_enter_pressed(event):
    threading.Thread(target=process_input).start()

input_entry.bind("<Return>", on_enter_pressed)

submit_button = ttk.Button(frame_input, text="送出", command=lambda: threading.Thread(target=process_input).start())
submit_button.pack(side=tk.RIGHT, padx=5)

def get_installed_models():
    try:
        result = subprocess.run(['ollama', 'list'], capture_output=True, text=True, creationflags=subprocess.CREATE_NO_WINDOW)
        models = result.stdout.strip().split('\n')
        models = [model.split()[0] for model in models if model]  # 解析名稱
        
        # 過濾掉不需要的選項（例如名為 "NAME" 的選項）
        filtered_models = [model for model in models if model != "NAME"]
        
        return filtered_models
    except Exception as e:
        messagebox.showerror("錯誤", f"無法獲取模型列表: {e}")
        return []

# 設置下拉選單的選項
models_combobox['values'] = get_installed_models()
if models_combobox['values']:
    models_combobox.current(0)  # 預設選擇第一個選項
else:
    chat_area.configure(state='normal')
    chat_area.insert('end', "請安裝至少一個 Ollama 模型。\n")
    chat_area.configure(state='disabled')

def typewriter_effect(text, sender):
    chat_area.configure(state='normal')
    chat_area.insert('end', f"{sender}：")
    chat_area.see('end')
    for char in text:
        chat_area.insert('end', char)
        chat_area.see('end')
        time.sleep(0.01)  # 控制字出現的速度
    chat_area.insert('end', '\n')
    chat_area.configure(state='disabled')
    chat_area.see('end')

def process_input():
    user_input = input_entry.get().strip()
    if not user_input:
        return  # 防止空輸入

    selected_model = models_combobox.get()
    if not selected_model:
        chat_area.configure(state='normal')
        chat_area.insert('end', "請先選擇一個模型。\n")
        chat_area.configure(state='disabled')
        return

    input_entry.delete(0, tk.END)  # 清除輸入框內容
    threading.Thread(target=typewriter_effect, args=(user_input, "您"), daemon=True).start()

    def run_model():
        try:
            response = subprocess.run(
                ['ollama', 'run', selected_model],
                input=user_input,
                capture_output=True,
                text=True,
                timeout=1500000,  # 設置超時時間
                creationflags=subprocess.CREATE_NO_WINDOW
            )

            if response.returncode == 0:
                threading.Thread(target=typewriter_effect, args=(response.stdout.strip(), selected_model), daemon=True).start()
            else:
                threading.Thread(target=typewriter_effect, args=(response.stderr.strip(), "錯誤"), daemon=True).start()
        except subprocess.TimeoutExpired:
            threading.Thread(target=typewriter_effect, args=("請求超時，請稍後再試。", "系統"), daemon=True).start()
        except Exception as e:
            threading.Thread(target=typewriter_effect, args=(f"發生錯誤：{str(e)}", "系統"), daemon=True).start()

    threading.Thread(target=run_model, daemon=True).start()


def on_closing():
    subprocess.Popen('taskkill /IM "ollama.exe" /F', shell=True)
    subprocess.Popen('taskkill /IM "ollama app.exe" /F', shell=True)
    chat_area.configure(state='normal')
    chat_area.insert('end', "系統：正在關閉應用程式...\n")
    chat_area.configure(state='disabled')
    chat_area.see('end')
    root.after(1000, root.destroy)  # 延遲 1 秒後關閉應用程式

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
