import tkinter as tk
from tkinter import ttk

def on_select(event):
    label.config(text=f"當前選擇: {combo.get()}")

root = tk.Tk()
root.title("Combobox 示範")

# 創建 Combobox
values = ["Python", "Java", "C++", "JavaScript"]
combo = ttk.Combobox(root, values=values, state="readonly")
combo.set("選擇程式語言")
combo.pack(pady=20)
combo.bind("<<ComboboxSelected>>", on_select)

# 顯示選擇結果
label = tk.Label(root, text="尚未選擇")
label.pack()

root.mainloop()