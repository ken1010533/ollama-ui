
import tkinter as tk # 載入 tkinter 模組
from 視窗至中模塊 import 視窗至中 # 載入視窗至中模組
import 語言設定模塊 # 載入語言設定模組
from tkinter import messagebox # 載入 messagebox 模組
def 設定視窗口():
    設定視窗的標題=語言設定模塊.語言['設定視窗標題'] # 設定視窗的標題
    設定的顏色切換=語言設定模塊.語言['顏色切換設定']['切換顏色'] # 設定的顏色切換
    設定的顏色切換_白色=語言設定模塊.語言['顏色切換設定']['白色'] # 設定的顏色切換_白色
    設定的顏色切換_黑色=語言設定模塊.語言['顏色切換設定']['黑色'] # 設定的顏色切換_黑色

    設定視窗 = tk.Tk() # 建立主視窗
    設定視窗.title(設定視窗的標題) # 設定主視窗標題
    視窗至中(設定視窗) # 設定視窗至中
###
    以切換到的顏色=tk.StringVar() # 建立字串變數
    顏色設定標題=tk.Label(設定視窗,text=設定的顏色切換) # 建立標籤
    顏色設定標題.pack() # 顯示標籤
    顏色＿白色=tk.Radiobutton(設定視窗,text=設定的顏色切換_白色,variable=以切換到的顏色,value=設定的顏色切換_白色) # 建立單選按鈕
    顏色＿黑色=tk.Radiobutton(設定視窗,text=設定的顏色切換_黑色,variable=以切換到的顏色,value=設定的顏色切換_黑色) # 建立單選按鈕
    顏色_白色.select() # 預設選擇白色
    顏色_白色.pack() # 顯示單選按鈕
    顏色_黑色.pack() # 顯示單選按鈕
    def 確認按鈕():
        print(以切換到的顏色.get()) # 印出選擇的顏色
        messagebox.showinfo("showinfo","重開後生效") # 顯示確認訊息
    
    
    確認按鈕鍵=tk.Button(設定視窗,text="確認",command=確認按鈕) # 建立按鈕
    確認按鈕鍵.pack() # 顯示按鈕
























    設定視窗.mainloop()

設定視窗口()