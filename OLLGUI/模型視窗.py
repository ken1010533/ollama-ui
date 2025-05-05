import tkinter as tk
from urllib.request import urlopen
from urllib.error import URLError
import webbrowser
from tkinter import   messagebox  # 載入 tkinter 模組
#from zmq import Frame  # 載入 tkinter 模組
from 模塊.視窗至中模塊 import 模型視窗至中  # 載入視窗至中模組
import 模塊.語言設定模塊 as 語言模型設定模塊  # 載入語言模型設定模塊
import 模塊.儲存設定檔 as 設定模塊  # 載入儲存模型設定檔模塊
import tkinter.ttk as ttk  # 載入 ttk 模組
import 模塊.收尋模型 as 收尋模型模塊  # 載入收尋模型以及版本模塊
import 模塊.可用模型版本 as 可用版本 # 載入語言設定模塊
import 模塊.刪除模型模塊 as 刪除模型模塊 # 載入刪除模型模塊
模型設定視窗 = None
def 模型設定視窗口():
    
    模型設定視窗的標題 = 語言模型設定模塊.語言['模型設定視窗標題']
    模型設定的取消按鈕 = 語言模型設定模塊.語言['模型設定的取消按鈕']
    模型設定的儲存並關閉按鈕 = 語言模型設定模塊.語言['模型設定的儲存並離開按鈕']

    模型設定的查詢按鈕 = 語言模型設定模塊.語言['模型設定的查詢按鈕']
    模型設定的詳細資訊 = 語言模型設定模塊.語言['模型設定的詳細資訊']
    模型設定的選擇模型 = 語言模型設定模塊.語言['模型設定的選擇模型']
    網路連線異常 = 語言模型設定模塊.語言['網路連線異常']
    請檢查網路連線或稍後再試 = 語言模型設定模塊.語言['請檢查網路連線或稍後再試']
    模型設定的管理模型按鈕 = 語言模型設定模塊.語言['管理模型按鈕']

    # 創建主視窗
    global 模型設定視窗
    if 模型設定視窗 is None or not 模型設定視窗.winfo_exists():
        模型設定視窗 = tk.Toplevel()
        模型設定視窗.title(模型設定視窗的標題)
        模型設定視窗.resizable(False,False)  # 設定視窗可調整大小
        模型視窗至中(模型設定視窗)  # 將視窗置中


    ### 讀取模型設定值 ###
    當前模型設定 = 設定模塊.讀取設定()  # 這裡會回傳 {"語言": ..., "顏色": ..., ...}
    def 更新模型設定並關閉():  # 確保模型存在
        設定模塊.寫入設定(**當前模型設定)
        模型設定視窗.destroy()
###
    # 模型格式
    模型單行輸入框跟查詢按鈕格式=tk.Frame(模型設定視窗) # 創建一個框架來放置單行輸入框和查詢按鈕
    模型單行輸入框跟查詢按鈕格式.place(rely=0.02,relwidth=1,height=25) # 設定位置和大小
 
    查尋模型結果選單格式=tk.Frame(模型設定視窗) # 創建一個框架來放置下拉選單
    查尋模型結果選單格式.place(relx=0.0,rely=0.35,relwidth=1) # 設定位置和大小

    以選擇模型跟詳細資訊格式=tk.Frame(模型設定視窗) # 創建一個框架來放置選擇模型和詳細資訊
    以選擇模型跟詳細資訊格式.place(relx=0.0,rely=0.2,relwidth=1,height=27) # 設定位置和大小

    
    # 模型單行輸入框和查詢按鈕
    模型單行輸入框=tk.Entry(模型單行輸入框跟查詢按鈕格式,font=("Arial", 10)) # 創建單行輸入框
    模型單行輸入框.place(relwidth=0.8,relheight=1) # 設定大小和位置
    def 查詢模型(): # 查詢模型的函數
        global 更多資訊網址 # 設定網址為空
        global 檢查網路連線
        def 檢查網路連線(測試網址="https://m.baidu.com", 等待時間=5):
            """
            檢查當前是否有網路連線
            參數:
                測試網址: 用於測試的網站地址（預設為Google）
                等待時間: 連接超時時間（秒）
            回傳:
                True 如果有網路連線，False 如果沒有
            """
            try:
                urlopen(測試網址, timeout=等待時間)
                return True
            except URLError:
                return False
        檢查網路連線() # 檢查網路連線
        if 檢查網路連線():
            print("✅ 網路連線正常")
            收尋模型模塊.網址 = f"https://ollama.com/search?q={模型單行輸入框.get()}" # 設定url
            收尋模型模塊.爬取網頁內容(收尋模型模塊.網址) # 爬取網頁內容
            url =收尋模型模塊.網址 # 設定url
            標題列表,標籤列表,資料筆數 = 收尋模型模塊.爬取網頁內容(url)
            print(資料筆數)
            查尋模型結果選單.set("") # 清空下拉選單
            查尋模型結果選單["values"] =標題列表 # 設定下拉選單的值
            更多資訊網址=收尋模型模塊.網址 # 設定網址
        else:
            messagebox.showerror(網路連線異常, 請檢查網路連線或稍後再試)
            print("❌ 網路連線異常，請檢查網路連線")
        

















    模型查詢按鈕=tk.Button(模型單行輸入框跟查詢按鈕格式,text=模型設定的查詢按鈕,font=("Arial", 10),command=查詢模型) # 創建查詢按鈕
    模型查詢按鈕.place(relx=0.8,relwidth=0.2,relheight=1) # 設定大小和位置


    def 顯示已選擇的模型(events): # 當選擇模型時更新標籤的文字
        以選擇模型.config(text=模型設定的選擇模型+查尋模型結果選單.get()) # 更新標籤的文字
        當前模型設定["查尋ollama模型結果"]=查尋模型結果選單.get()
        以選擇的查詢模型結果.set('')  # 清空當前顯示的值
        以選擇的查詢模型結果['values'] = []  # 清空下拉選單的值
        global 更多資訊網址
        更多資訊網址 = None
        預設1模型 =查尋模型結果選單.get()  # 手動設置預設模型名稱為 'qwq'，避免它成為函式
        模型版本網址 = f"https://ollama.com/library/{預設1模型}/tags"
        版本列表 = 可用版本.搜尋模組版本(模型版本網址)
        if isinstance(版本列表, tuple) and len(版本列表) == 3:
            版本資料 = 版本列表[0]  # 取得模型版本資料（列表）
            計數 = 版本列表[1]  # 取得計數
            模型版本網址 = 版本列表[2]  # 取得網址

            # 現在開始處理版本資料
            if 版本資料:
                模型版本名稱=[]
                for 版本 in 版本資料:
                    if isinstance(版本, tuple) and len(版本) == 4:
                        名稱, 編號, 容量, 發佈時間 = 版本
                        print(f"名稱: {名稱}")
                        print(f"編號: {編號}")
                        print(f"容量: {容量}")
                        print(f"發佈時間: {發佈時間}")
                        print("--------")
                        模型版本名稱.append(名稱)
                    else:
                        print("找到非預期的資料格式:", 版本)


            print(f"目前共找到 {計數} 筆模型版本資料")
            print("--------")
            print(模型版本網址)  # 印出網址
            更多資訊網址=f"https://ollama.com/library/{預設1模型}"
            以選擇的查詢模型結果['values'] =模型版本名稱
        else:
            print("版本列表格式錯誤:", 版本列表)







    查尋模型結果選單=ttk.Combobox(查尋模型結果選單格式,state="readonly",font=("Arial", 10)) # 創建下拉選單
    查尋模型結果選單.pack(fill=tk.X, padx=1.5, pady=1.5)    # 設定大小和位置
    查尋模型結果選單.bind("<<ComboboxSelected>>",顯示已選擇的模型) # 當選擇模型時更新標籤的文字

    def 更新以選擇的查詢模型結果(event): # 當選擇模型時更新標籤的文字
        global 更多資訊網址
        以選擇模型.config(text=模型設定的選擇模型+查尋模型結果選單.get()+" : "+以選擇的查詢模型結果.get()) # 更新標籤的文字
        當前模型設定["查尋ollama模型結果"]=查尋模型結果選單.get()+":"+以選擇的查詢模型結果.get()
        更多資訊網址="https://ollama.com/library/"+查尋模型結果選單.get()+":"+以選擇的查詢模型結果.get()

    以選擇的查詢模型結果=ttk.Combobox(查尋模型結果選單格式,state="readonly",font=("Arial", 10)) # 創建下拉選單
    以選擇的查詢模型結果.pack(fill=tk.X, padx=1.5, pady=1.5)    # 設定大小和位置
    以選擇的查詢模型結果.bind("<<ComboboxSelected>>",更新以選擇的查詢模型結果) # 當選擇模型時更新標籤的文字

    以選擇模型=tk.Label(以選擇模型跟詳細資訊格式,text=模型設定的選擇模型+查尋模型結果選單.get(),font=("Arial", 11)) # 創建標籤
    以選擇模型.pack(fill=tk.X, padx=1.5, pady=0.5,side="left")  # 設定大小和位置

    

    global 更多資訊網址 # 設定網址為空
    更多資訊網址=None # 設定網址為空
    def 更多資訊():
        
        if not 檢查網路連線():
            messagebox.showerror(網路連線異常, 請檢查網路連線或稍後再試)
            print("❌ 網路連線異常，請檢查網路連線")
            return
        global 更多資訊網址
        if 更多資訊網址 is None:
            webbrowser.open("https://ollama.com/")
        webbrowser.open(更多資訊網址)
        return 更多資訊網址

    以選擇模型的詳細資訊=tk.Button(以選擇模型跟詳細資訊格式,text=模型設定的詳細資訊,font=("Arial", 10),command=更多資訊) # 創建詳細資訊按鈕
    以選擇模型的詳細資訊.pack(fill=tk.X, padx=1.5, pady=1,side="right") # 設定大小和位置




    def 管理模型():
       刪除模型模塊.刪除頁面視窗()

    取消和儲存並關閉按鈕=tk.Frame(模型設定視窗) # 創建一個框架來放置取消和儲存並關閉按鈕
    取消和儲存並關閉按鈕.place(relx=0.98,rely=0.98,anchor="se")     # 設定位置和大小
    
    管理模型按鈕=tk.Button(取消和儲存並關閉按鈕,text=模型設定的管理模型按鈕,font=("Arial", 10),command=管理模型) # 創建管理模型按鈕
    管理模型按鈕.grid(column=0, row=0, sticky="ew", padx=8, pady=0.1) # 設定大小和位置
    # 按鈕
    取消按鈕 = tk.Button(取消和儲存並關閉按鈕, text=模型設定的取消按鈕, command=模型設定視窗.destroy)  # 創建取消按鈕
    取消按鈕.grid(column=1, row=0, sticky="ew", padx=8, pady=0.1)  # 設定大小和位置
    
    儲存並關閉按鈕 = tk.Button(取消和儲存並關閉按鈕, text=模型設定的儲存並關閉按鈕, command=更新模型設定並關閉)  # 創建儲存並關閉按鈕
    儲存並關閉按鈕.grid(column=2, row=0, sticky="ew", padx=0.1, pady=0.1)  # 設定大小和位置

   # 開始主循環，等待事件發生
    模型設定視窗.mainloop()  # 啟動主循環，等待事件發生   