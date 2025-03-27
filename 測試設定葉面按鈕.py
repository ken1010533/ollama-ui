import tkinter as tk
from tkinter import ttk

def save_settings():
    print("設定已儲存：")
    print(f"語言: {language_combobox.get()}")
    print(f"主題: {theme_var.get()}")
    print(f"自動更新: {auto_update_var.get()}")

# 創建主視窗
root = tk.Tk()
root.title("PGT 設定頁面")

# 使用 Notebook 實現分頁
notebook = ttk.Notebook(root)
notebook.pack(padx=10, pady=10, fill="both", expand=True)

# 分頁 1：基本設定
general_frame = ttk.Frame(notebook)
notebook.add(general_frame, text="基本設定")

# 語言選擇
ttk.Label(general_frame, text="語言:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
language_combobox = ttk.Combobox(general_frame, values=["繁體中文", "English", "日本語"])
language_combobox.grid(row=0, column=1, padx=5, pady=5)
language_combobox.set("繁體中文")

# 主題選擇
ttk.Label(general_frame, text="主題:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
theme_var = tk.StringVar(value="dark")
ttk.Radiobutton(general_frame, text="深色模式", variable=theme_var, value="dark").grid(row=1, column=1, sticky="w")
ttk.Radiobutton(general_frame, text="淺色模式", variable=theme_var, value="light").grid(row=2, column=1, sticky="w")

# 自動更新
auto_update_var = tk.BooleanVar(value=True)
ttk.Checkbutton(general_frame, text="啟用自動更新", variable=auto_update_var).grid(row=3, column=0, columnspan=2, sticky="w")

# 分頁 2：編輯器設定
editor_frame = ttk.Frame(notebook)
notebook.add(editor_frame, text="編輯器設定")

ttk.Label(editor_frame, text="字型大小:").grid(row=0, column=0, padx=5, pady=5)
font_size = tk.Scale(editor_frame, from_=8, to=24, orient="horizontal")
font_size.grid(row=0, column=1, padx=5, pady=5)

# 儲存按鈕
save_button = ttk.Button(root, text="儲存設定", command=save_settings)
save_button.pack(pady=10)

root.mainloop()