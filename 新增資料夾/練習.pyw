#region

# 宣告使用的函式庫
from time import sleep
import tkinter as tk
#import ctypes
import subprocess
import threading
import tkinter.ttk as ttk
from tkinter import messagebox
import ollama安裝檢查
import 模型設定視窗
from 模型設定視窗 import 選定模型

#######################################################################################################
# 创建窗口
root = tk.Tk()                             # 创建主窗口
root.title("功能丰富的 GUI 应用 - 正在使用模型 " + 選定模型.get()) 
標題=root.title    # 設定視窗標題
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
#ctypes.windll.kernel32.FreeConsole()      # 隱藏命令提示字元視窗
frame3 = tk.Frame(root) # 創建 Frame
frame3.pack(side="bottom", fill="both") # 將 Frame 放置在視窗
frame1 = tk.Frame(root) # 創建 Frame
frame1.pack(side='bottom', fill="both") # 將 Frame 放置在視窗
frame2 = tk.Frame(root) # 創建 Frame
frame2.pack(side='top', fill="both") # 將 Frame 放置在視窗
frame4 = None # 創建 Frame 4 用來放置模型設定視窗
frame5 = None # 創建 Frame 5 用來放置模型設定視窗
frame6 = None # 創建 Frame 6 用來放置模型設定視窗
subprocess.Popen('taskkill /IM "ollama.exe" /F', shell=True)
subprocess.Popen('taskkill /IM "ollama app.exe" /F', shell=True)
#######################################################################################################
#檢查檔案完整性
#region
if not ollama安裝檢查.檢查_ollama_是否安裝():
    messagebox.showerror("錯誤", "請檢查檔案完整性\"選項---->檢查\"")
    root.destroy()
#endregion
#######################################################################################################
    #輸入框
#region 
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

def send_message(event=None):
    user_input = text.get("1.0", tk.END).strip()
    if user_input and user_input != default_text:
        if not 模型設定視窗.選定模型():  # 假設這是檢查模型是否選擇的函數
            messagebox.showerror("錯誤", "請先選擇模型")
        else:
            output_text.config(state=tk.NORMAL)
            output_text.insert(tk.END, f"User: {user_input}\n")
            output_text.config(state=tk.DISABLED)
            text.delete("1.0", tk.END)
            text.insert("1.0", default_text)
            text.config(fg="gray", insertbackground="gray")

# 創建 Text 元件（wrap="word" 讓文字自動換行）
text = tk.Text(frame1, wrap="word", height=1, relief="ridge", borderwidth=3) # 創建 Text
text.grid(column=3, row=2, sticky="nsew", pady=10)  # 讓 Text 填滿 Frame

text.insert("1.0", default_text)  # 插入提示文字
text.config(fg="gray", insertbackground="gray")  # 初始顏色變淡
text.bind("<FocusIn>", on_text_focus_in)  # 當點擊輸入框時
text.bind("<FocusOut>", on_text_focus_out)  # 當離開輸入框時
text.bind("<Return>", send_message)  # 綁定 Enter 鍵

scrollbar = tk.Scrollbar(frame1, command=text.yview)  # 創建 Scrollbar
text.config(yscrollcommand=scrollbar.set) # 讓 Text 與 Scrollbar 連動
frame1.grid_rowconfigure(2, weight=1) # 設定第 2 列的高度可變動
frame1.grid_columnconfigure(3, weight=1) # 設定第 3 欄的寬度可變動

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
#endregion

#######################################################################################################

#聊天功能
#region



#endregion

#######################################################################################################
# 輸出文字框
    #region 

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
#endregion
#######################################################################################################

    #畫布功能
#region 

畫布功能=tk.Button(frame3, text="畫布功能", command=lambda: messagebox.showerror("功能尚未開放", "功能尚未開放"))
畫布功能.grid(column=5, row=5)
#endregion 
#######################################################################################################
   
    #控制台功能
#region


控制台功能=tk.Button(frame3, text="控制台功能", command=lambda: messagebox.showerror("功能尚未開放", "功能尚未開放"))
控制台功能.grid(column=6, row=5)    


#endregion

#######################################################################################################
#模型設定視窗
#region
def 模型開():
    模型設定視窗.模型設定()
    sleep(1)
模型設定_btn = tk.Button(frame3, text="模型設定", command=模型開)
模型設定_btn.grid(column=4, row=5)
#endregion
#######################################################################################################
        # 菜單
  #region      
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
#endregion
#######################################################################################################

#設定按鈕
#region
root.tk.call("ttk::style", "theme", "use", "alt")
frame1.config(bg="#3C3C3C")
frame2.config(bg="#3C3C3C")
frame3.config(bg="#3C3C3C")
text.config(bg="#3C3C3C", fg="white", insertbackground="white")
output_text.config(bg="#3C3C3C", fg="white")

def toggle():
    toggle_theme()
    toggle_theme1()
    toggle_theme2()
    toggle_theme3()

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
def toggle_theme2():  
    current_theme = root.tk.call("ttk::style", "theme", "use" )     
    if current_theme == "clam":
        if frame5 is not None and frame5.winfo_exists():
             frame5.config(bg="white")
    else:
        if frame5 is not None and frame5.winfo_exists():
            frame5.config(bg="#3C3C3C")
def toggle_theme3():  
    current_theme = root.tk.call("ttk::style", "theme", "use" )     
    if current_theme == "clam":
        if frame6 is not None and frame6.winfo_exists():
             frame6.config(bg="white")
    else:
        if frame6 is not None and frame6.winfo_exists():
            frame6.config(bg="#3C3C3C")

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
#endregion



#######################################################################################################

    #關閉應用程式
#region
def on_closing():
    subprocess.Popen('taskkill /IM "ollama.exe" /F', shell=True)
    subprocess.Popen('taskkill /IM "ollama app.exe" /F', shell=True)
    root.after(1000, root.destroy)  # 延遲 1 秒後關閉應用程式

root.protocol("WM_DELETE_WINDOW", on_closing)

#endregion
#######################################################################################################
    # 窗口运行

root.mainloop() 
#######################################################################################################

#######################################################################################################