import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import subprocess
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

# 創建選單框架
menu_frame = tk.Frame(root, width=100, bg="lightgray")
menu_frame.pack(side="left", fill="y")

# 在選單框架中添加一些按鈕
for i in range(5):
    button = tk.Button(menu_frame, text=f"選項 {i+1}")
    button.pack(pady=5)

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
        return models
    except Exception as e:
        messagebox.showerror("錯誤", f"無法獲取模型列表: {e}")
        return []

models_combobox['values'] = get_installed_models()
if models_combobox['values']:
    models_combobox.current(1)  # 預設選擇第一個
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

    if user_input.lower() == "/bye":
        on_closing()
        return

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
    chat_area.configure(state='normal')
    chat_area.insert('end', "系統：正在關閉應用程式...\n")
    chat_area.configure(state='disabled')
    chat_area.see('end')
    root.after(1000, root.destroy)  # 延遲 1 秒後關閉

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
