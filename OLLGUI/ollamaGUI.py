import tkinter as tk
from tkinter import ttk
import json
import 讀檔

設定檔 = "設定.json"

def 讀取設定():
    try:
        with open(設定檔, "r", encoding="utf-8") as f:
            return json.load(f).get("語言", "zh-TW")
    except FileNotFoundError:
        return "zh-TW"

def 儲存設定(語言):
    with open(設定檔, "w", encoding="utf-8") as f:
        json.dump({"語言": 語言}, f)

def 設定視窗口():
    設定視窗 = tk.Tk()
    設定視窗.title("設定")

    當前語言 = 讀取設定()

    def 更新語言(event):
        儲存設定(語言選單.get())

    ttk.Label(設定視窗, text="選擇語言:").pack()
    語言選單 = ttk.Combobox(設定視窗, values=讀檔.語言翻譯)
    語言選單.pack()
    語言選單.set(當前語言)
    語言選單.bind("<<ComboboxSelected>>", 更新語言)

    設定視窗.mainloop()
