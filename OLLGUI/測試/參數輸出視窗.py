import tkinter as tk
from tkinter import ttk
from config import 參數紀錄

def 顯示參數結果():
    視窗 = tk.Tk()
    視窗.title("目前參數與結果")
    視窗.geometry("500x400")

    標題 = tk.Label(視窗, text="🔧 目前設定參數與結果", font=("Arial", 14))
    標題.pack(pady=10)

    表格 = ttk.Treeview(視窗, columns=("參數", "值"), show='headings')
    表格.heading("參數", text="參數")
    表格.heading("值", text="值")
    表格.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    for key, value in 參數紀錄.items():
        表格.insert('', tk.END, values=(key, value))

    關閉按鈕 = tk.Button(視窗, text="關閉", command=視窗.destroy)
    關閉按鈕.pack(pady=10)

    視窗.mainloop()
