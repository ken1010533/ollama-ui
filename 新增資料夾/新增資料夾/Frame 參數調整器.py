import tkinter as tk
from tkinter import ttk

# 創建主視窗
root = tk.Tk()
root.title("Frame 參數調整器")
root.geometry("600x400")

# 預設參數
frame_options = {
    "bg": "lightblue",
    "bd": 2,
    "relief": "ridge",
    "width": 200,
    "height": 150,
    "padx": 10,
    "pady": 10,
    "cursor": "arrow"
}

# 創建 Frame
frame = tk.Frame(root, **frame_options)
frame.pack(pady=20)

# 更新 Frame 設定的函數
def update_frame():
    frame.config(
        bg=bg_var.get(),
        bd=int(bd_var.get()),
        relief=relief_var.get(),
        width=int(width_var.get()),
        height=int(height_var.get()),
        padx=int(padx_var.get()),
        pady=int(pady_var.get()),
        cursor=cursor_var.get()
    )
    frame.pack_configure(padx=int(padx_var.get()), pady=int(pady_var.get()))

# 設定選項 UI
control_panel = tk.Frame(root)
control_panel.pack()

# 背景顏色
tk.Label(control_panel, text="背景顏色:").grid(row=0, column=0)
bg_var = tk.StringVar(value=frame_options["bg"])
bg_entry = tk.Entry(control_panel, textvariable=bg_var)
bg_entry.grid(row=0, column=1)

# 邊框寬度
tk.Label(control_panel, text="邊框寬度:").grid(row=1, column=0)
bd_var = tk.StringVar(value=str(frame_options["bd"]))
bd_entry = tk.Entry(control_panel, textvariable=bd_var)
bd_entry.grid(row=1, column=1)

# 邊框樣式
tk.Label(control_panel, text="邊框樣式:").grid(row=2, column=0)
relief_var = tk.StringVar(value=frame_options["relief"])
relief_menu = ttk.Combobox(control_panel, textvariable=relief_var, values=["flat", "raised", "sunken", "ridge", "solid", "groove"])
relief_menu.grid(row=2, column=1)

# 寬度
tk.Label(control_panel, text="寬度:").grid(row=3, column=0)
width_var = tk.StringVar(value=str(frame_options["width"]))
width_entry = tk.Entry(control_panel, textvariable=width_var)
width_entry.grid(row=3, column=1)

# 高度
tk.Label(control_panel, text="高度:").grid(row=4, column=0)
height_var = tk.StringVar(value=str(frame_options["height"]))
height_entry = tk.Entry(control_panel, textvariable=height_var)
height_entry.grid(row=4, column=1)

# 內邊距 padx
tk.Label(control_panel, text="內邊距 padx:").grid(row=5, column=0)
padx_var = tk.StringVar(value=str(frame_options["padx"]))
padx_entry = tk.Entry(control_panel, textvariable=padx_var)
padx_entry.grid(row=5, column=1)

# 內邊距 pady
tk.Label(control_panel, text="內邊距 pady:").grid(row=6, column=0)
pady_var = tk.StringVar(value=str(frame_options["pady"]))
pady_entry = tk.Entry(control_panel, textvariable=pady_var)
pady_entry.grid(row=6, column=1)

# 滑鼠指標
tk.Label(control_panel, text="滑鼠指標:").grid(row=7, column=0)
cursor_var = tk.StringVar(value=frame_options["cursor"])
cursor_menu = ttk.Combobox(control_panel, textvariable=cursor_var, values=["arrow", "hand2", "cross", "circle", "xterm"])
cursor_menu.grid(row=7, column=1)

# 更新按鈕
update_btn = tk.Button(control_panel, text="更新 Frame", command=update_frame)
update_btn.grid(row=8, column=0, columnspan=2, pady=10)

root.mainloop()
