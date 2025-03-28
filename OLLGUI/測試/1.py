import tkinter as tk

root = tk.Tk()
language_var = tk.StringVar(value="繁體中文")  # 預設選中繁體中文

# 單選按鈕群組
tk.Radiobutton(root, text="繁體中文", variable=language_var, value="繁體中文").pack()
tk.Radiobutton(root, text="English", variable=language_var, value="English").pack()
tk.Radiobutton(root, text="日本語", variable=language_var, value="日本語").pack()

root.mainloop()