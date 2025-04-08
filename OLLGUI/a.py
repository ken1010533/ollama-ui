import tkinter as tk

root = tk.Tk()
root.title("混合布局範例")
root.geometry("500x400")

# 頂部工具欄 (pack)
toolbar = tk.Frame(root, bg="lightblue", height=40)
toolbar.pack(side="top", fill="x")

btn_file = tk.Button(toolbar, text="檔案")
btn_file.pack(side="left", padx=5, pady=5)

btn_edit = tk.Button(toolbar, text="編輯")
btn_edit.pack(side="left", padx=5, pady=5)

# 主內容區 (pack)
main_area = tk.Frame(root, bg="white")
main_area.pack(expand=True, fill="both", padx=5, pady=5)

# 左側導航欄 (grid)
left_nav = tk.Frame(main_area, bg="lightgreen", width=100)
left_nav.grid(row=0, column=0, sticky="ns", rowspan=2)

for i in range(5):
    btn = tk.Button(left_nav, text=f"選項{i+1}")
    btn.pack(fill="x", padx=2, pady=2)

# 右側內容區 (grid)
content = tk.Frame(main_area, bg="lightyellow")
content.grid(row=0, column=1, sticky="nsew")

# 使用place在內容區精確定位
label1 = tk.Label(content, text="標題", bg="yellow")
label1.place(relx=0.5, rely=0.1, anchor="center")

text = tk.Text(content, bg="white")
text.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.6)

# 底部狀態欄 (pack)
status = tk.Label(root, text="就緒", bg="lightgray", bd=1, relief="sunken", anchor="w")
status.pack(side="bottom", fill="x")

# 配置grid權重
main_area.grid_columnconfigure(1, weight=1)
main_area.grid_rowconfigure(0, weight=1)

root.mainloop()