import tkinter.ttk as ttk
from tkinter import messagebox
# 在分頁本模塊.py中使用
# 在分頁本模塊.py中使用
from 主視窗 import 主視窗
import 模塊.語言設定模塊 as 語言設定模塊
import tkinter as tk















def 分頁本():
    主視窗的取消按鈕 = 語言設定模塊.語言['主視窗的關閉按鈕']
    主視窗的儲存並關閉按鈕 = 語言設定模塊.語言['主視窗的儲存並離開按鈕']

    # 建立 Notebook 樣式
    聊天視窗格式 = ttk.Style()
    聊天視窗格式.configure("TNotebook", tabposition='wn')

    聊天視窗 = ttk.Notebook(主視窗, style='TNotebook')
    聊天視窗.pack(expand=True, fill="both")

    # 🔽 關閉分頁函式（會取得當前選取的頁面）
    def 關閉目前分頁():
        所有分頁 = 聊天視窗.tabs()
        if len(所有分頁) <= 1:
            messagebox.showwarning("警告", "最後一個分頁不能關閉！")
            return

        當前分頁 = 聊天視窗.select()
        聊天視窗.forget(當前分頁)

    # 🔽 新增分頁函式
    def 新增分頁():
        新頁面 = ttk.Frame(聊天視窗)
        聊天視窗.add(新頁面, text="新聊天")
        聊天視窗.select(新頁面)  # 自動切換到新分頁

        # 加入分頁內容
        取消和儲存並關閉按鈕 = tk.Frame(新頁面)
        取消和儲存並關閉按鈕.place(relx=0.98, rely=0.98, anchor="se")

        # 取消（關閉分頁）按鈕
        取消按鈕 = tk.Button(取消和儲存並關閉按鈕, text=主視窗的取消按鈕, command=關閉目前分頁)
        取消按鈕.grid(column=0, row=0, sticky="ew", padx=8, pady=0.1)

        # 儲存並關閉（這裡是測試：直接新增下一頁）
        儲存並關閉按鈕 = tk.Button(取消和儲存並關閉按鈕, text=主視窗的儲存並關閉按鈕, command=新增分頁)
        儲存並關閉按鈕.grid(column=1, row=0, sticky="ew", padx=0.1, pady=0.1)

    # 預設加入一頁
    新增分頁()
