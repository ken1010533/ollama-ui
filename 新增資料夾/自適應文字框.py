import tkinter as tk
from tkinter import ttk
import json

# 讀取語言檔案
def load_languages():
    with open("languages.json", "r", encoding="utf-8") as file:
        return json.load(file)

languages = load_languages()  # 讀取 JSON 檔案
language_list = list(languages.keys())  # 取得所有語言代碼
current_language = language_list[0]  # 預設第一種語言

def switch_language(event=None):
    global current_language
    # 取得選擇的語言
    current_language = language_combobox.get()
    # 更新按鈕文字
    language_button.config(text=languages[current_language]["language_button"])

# 建立主視窗
root = tk.Tk()
root.title("語言切換（下拉選單版）")

# 建立框架
frame = ttk.Frame(root)
frame.pack(padx=20, pady=20)

# 創建下拉選單
language_combobox = ttk.Combobox(frame, values=language_list, state="readonly")
language_combobox.set(current_language)  # 設定預設值
language_combobox.pack(pady=5)
language_combobox.bind("<<ComboboxSelected>>", switch_language)  # 綁定選擇事件

# 建立按鈕
language_button = ttk.Button(frame, text=languages[current_language]["language_button"])
language_button.pack(pady=10, anchor="center", expand=True, fill="both", ipadx=10, ipady=10)

# 啟動主迴圈
root.mainloop()
