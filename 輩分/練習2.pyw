# 宣告使用的函式庫
import tkinter as tk
import ctypes
import subprocess


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
frame1 = tk.Frame(root) # 創建 Frame
frame1.pack(side='bottom', fill="both") # 將 Frame 放置在視窗

# 創建 Text 元件（wrap="word" 讓文字自動換行）
text = tk.Text(frame1, wrap="word", height=1, relief="ridge", borderwidth=3)
text.grid(column=3, row=2, sticky="nsew", padx=10, pady=10)  # 讓 Text 填滿 Frame


# 滾動條
scrollbar = tk.Scrollbar(frame1, command=text.yview)

# 綁定滾動條
text.config(yscrollcommand=scrollbar.set)

# 讓 Frame 內的 Text 自動調整大小
frame1.grid_rowconfigure(2, weight=1)
frame1.grid_columnconfigure(3, weight=1)

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

def set1():
   pass
def set2():
    pass
def set3():
    on_closing()

菜單=tk.Menu(root)  # 创建菜单
設定子菜單=tk.Menu(菜單,tearoff=0)  # 创建子菜单
設定子菜單.add_command(label="設定1",command=set1)  # 添加子菜单命令
設定子菜單.add_command(label="設定2",command=set2)
設定子菜單.add_command(label="離開",command=set3)
菜單.add_cascade(label="選項",menu=設定子菜單)  # 添加子菜单到菜单

def info1():
   pass
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


def on_closing():
    subprocess.Popen('taskkill /IM "ollama.exe" /F', shell=True)
    subprocess.Popen('taskkill /IM "ollama app.exe" /F', shell=True)
    root.after(1000, root.destroy)  # 延遲 1 秒後關閉應用程式

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()  # 窗口运行
