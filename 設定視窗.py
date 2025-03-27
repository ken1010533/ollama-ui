from operator import truediv
import tkinter as tk  # 載入 tkinter 模組
from 視窗至中模塊 import 視窗至中  # 載入視窗至中模組
import 語言設定模塊  # 載入語言設定模組
from tkinter import ttk  # 載入 ttk 模組
import 讀檔  # 載入讀檔模組 (請確認名稱)
import json

設定檔="set.json"

def 讀取設定():
    try:
        with open(設定檔, "r",encoding="utf-8") as f:
            return json.load(f).get("語言","繁體中文")
    except FileNotFoundError:
        return "繁體中文"
    
def 寫入設定(語言):
    with open(設定檔, "w",encoding="utf-8") as f:
        json.dump({"語言":語言},f)



































def 設定視窗口():
    設定視窗的標題 = 語言設定模塊.語言['設定視窗標題']  # 設定視窗的標題
    設定的顏色切換 = 語言設定模塊.語言['顏色切換設定']['切換顏色']  # 設定顏色切換標題
    設定的顏色切換_白色 = 語言設定模塊.語言['顏色切換設定']['白色']  # 白色選項
    設定的顏色切換_黑色 = 語言設定模塊.語言['顏色切換設定']['黑色']  # 黑色選項
    設定的語言翻譯 = 語言設定模塊.語言['語言選單']  # 語言選單標題
    
###

    # 創建主視窗
    設定視窗 = tk.Tk()
    設定視窗.title(設定視窗的標題)
    視窗至中(設定視窗)  # 設定視窗至中

    # 顏色切換設定
    顏色設定標題 = tk.Label(設定視窗, text=設定的顏色切換)
    顏色設定標題.pack()
    以切換到的顏色 = tk.StringVar(value=設定的顏色切換_白色)  # 預設為白色
    顏色_白色 = tk.Radiobutton(設定視窗, text=設定的顏色切換_白色, variable=以切換到的顏色, value=設定的顏色切換_白色)
    顏色_黑色 = tk.Radiobutton(設定視窗, text=設定的顏色切換_黑色, variable=以切換到的顏色, value=設定的顏色切換_黑色)
    
    顏色_白色.pack()
    顏色_黑色.pack()
####################

    當前語言=讀取設定()

    def 更新語言(event):
        處存設定(語言選單.get())




    # 語言選單
    global 語言選單
    ttk.Label(設定視窗, text=設定的語言翻譯).pack()
    語言選單 = ttk.Combobox(設定視窗, values=讀檔.語言翻譯)  # 從讀檔模組獲取可選語言
    語言選單.pack()
    語言選單.set(當前語言)  # 預設選擇繁體中文
    語言選單.bind("<<ComboboxSelected>>", 更新語言)  # 當選擇語言時，執行語言選擇函數
    設定視窗.mainloop() # 顯示視窗

設定視窗口()  # 如果要執行，解除註解
