import tkinter as tk
from 單一視窗模塊 import 單一視窗

def 建立子視窗11內容(視窗):
    標籤 = tk.Label(視窗, text="這是子視窗")
    標籤.pack(padx=20, pady=20)

def 主程式():
    主視窗 = tk.Tk()
    主視窗.title("主視窗")

    子視窗 = 單一視窗(主視窗, 標題="設定")

    按鈕 = tk.Button(主視窗, text="打開設定視窗", command=lambda: 子視窗.顯示(建立子視窗11內容))
    按鈕.pack(pady=20)

    主視窗.mainloop()

if __name__ == "__main__":
    主程式()
