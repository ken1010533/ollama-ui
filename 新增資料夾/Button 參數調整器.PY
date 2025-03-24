import tkinter as tk
from tkinter import ttk

# 創建主視窗
root = tk.Tk()
root.title("Button 參數調整器")
root.geometry("600x500")

# 預設按鈕參數
button_options = {
    "text": "點我！",
    "bg": "lightgreen",
    "fg": "black",
    "bd": 5,
    "relief": "raised",
    "width": 20,
    "height": 2,
    "font": ("Arial", 14),
    "cursor": "hand2",
    "padx": 10,
    "pady": 10
}

# 創建按鈕
button = tk.Button(root, **button_options)
button.pack(pady=20)

# 更新按鈕設定的函數
def update_button():
    button.config(
        text=text_var.get(),
        bg=bg_var.get(),
        fg=fg_var.get(),
        bd=int(bd_var.get()),
        relief=relief_var.get(),
        width=int(width_var.get()),
        height=int(height_var.get()),
        font=(font_var.get(), int(font_size_var.get())),
        cursor=cursor_var.get(),
        padx=int(padx_var.get()),
        pady=int(pady_var.get())
    )

# 設定選項 UI
control_panel = tk.Frame(root)
control_panel.pack()

# 按鈕文字
tk.Label(control_panel, text="按鈕文字:").grid(row=0, column=0)
text_var = tk.StringVar(value=button_options["text"])
text_entry = tk.Entry(control_panel, textvariable=text_var)
text_entry.grid(row=0, column=1)

# 背景顏色
tk.Label(control_panel, text="背景顏色:").grid(row=1, column=0)
bg_var = tk.StringVar(value=button_options["bg"])
bg_entry = tk.Entry(control_panel, textvariable=bg_var)
bg_entry.grid(row=1, column=1)

# 文字顏色
tk.Label(control_panel, text="文字顏色:").grid(row=2, column=0)
fg_var = tk.StringVar(value=button_options["fg"])
fg_entry = tk.Entry(control_panel, textvariable=fg_var)
fg_entry.grid(row=2, column=1)

# 邊框寬度
tk.Label(control_panel, text="邊框寬度:").grid(row=3, column=0)
bd_var = tk.StringVar(value=str(button_options["bd"]))
bd_entry = tk.Entry(control_panel, textvariable=bd_var)
bd_entry.grid(row=3, column=1)

# 邊框樣式
tk.Label(control_panel, text="邊框樣式:").grid(row=4, column=0)
relief_var = tk.StringVar(value=button_options["relief"])
relief_menu = ttk.Combobox(control_panel, textvariable=relief_var, values=["flat", "raised", "sunken", "ridge", "solid", "groove"])
relief_menu.grid(row=4, column=1)

# 寬度
tk.Label(control_panel, text="寬度:").grid(row=5, column=0)
width_var = tk.StringVar(value=str(button_options["width"]))
width_entry = tk.Entry(control_panel, textvariable=width_var)
width_entry.grid(row=5, column=1)

# 高度
tk.Label(control_panel, text="高度:").grid(row=6, column=0)
height_var = tk.StringVar(value=str(button_options["height"]))
height_entry = tk.Entry(control_panel, textvariable=height_var)
height_entry.grid(row=6, column=1)

# 字體名稱
tk.Label(control_panel, text="字體名稱:").grid(row=7, column=0)
font_var = tk.StringVar(value=button_options["font"][0])
font_entry = tk.Entry(control_panel, textvariable=font_var)
font_entry.grid(row=7, column=1)

# 字體大小
tk.Label(control_panel, text="字體大小:").grid(row=8, column=0)
font_size_var = tk.StringVar(value=str(button_options["font"][1]))
font_size_entry = tk.Entry(control_panel, textvariable=font_size_var)
font_size_entry.grid(row=8, column=1)

# 滑鼠指標
tk.Label(control_panel, text="滑鼠指標:").grid(row=9, column=0)
cursor_var = tk.StringVar(value=button_options["cursor"])
cursor_menu = ttk.Combobox(control_panel, textvariable=cursor_var, values=["arrow", "hand2", "cross", "circle", "xterm"])
cursor_menu.grid(row=9, column=1)

# 內邊距 padx
tk.Label(control_panel, text="內邊距 padx:").grid(row=10, column=0)
padx_var = tk.StringVar(value=str(button_options["padx"]))
padx_entry = tk.Entry(control_panel, textvariable=padx_var)
padx_entry.grid(row=10, column=1)

# 內邊距 pady
tk.Label(control_panel, text="內邊距 pady:").grid(row=11, column=0)
pady_var = tk.StringVar(value=str(button_options["pady"]))
pady_entry = tk.Entry(control_panel, textvariable=pady_var)
pady_entry.grid(row=11, column=1)

# 更新按鈕
update_btn = tk.Button(control_panel, text="更新按鈕", command=update_button)
update_btn.grid(row=12, column=0, columnspan=2, pady=10)

# 新增的功能
n = 1.1               # n 等於 0
a = tk.StringVar()  # 設定 a 為文字變數
a.set(n)            # 設定 a 的內容

def add():
    global n        # n 是全域變數
    n = n  *(1+n)       # 每次執行 add 時將 n 增加 1
    a.set(n)        # 設定 a 的內容

mylabel = tk.Label(root, textvariable=a, font=('Arial',20))  # 放入標籤
mylabel.pack()

# Button 設定 command 參數
btn = tk.Button(root,
                text='我是按鈕',
                font=('Arial',30,'bold'),
                command=add
              )
btn.pack()

root.mainloop()
