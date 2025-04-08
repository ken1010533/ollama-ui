import tkinter as tk

#from zmq import Frame  # 載入 tkinter 模組
from 模塊.視窗至中模塊 import 模型視窗至中  # 載入視窗至中模組
import 模塊.語言設定模塊 as 語言模型設定模塊  # 載入語言模型設定模塊
import 模塊.儲存設定檔 as 設定模塊  # 載入儲存模型設定檔模塊
import tkinter.ttk as ttk  # 載入 ttk 模組
import 模塊.收尋模型以及版本 as 收尋模型模塊  # 載入收尋模型以及版本模塊
import 模塊.可用模型版本 as 可用版本 # 載入語言設定模塊
def 模型設定視窗口():
    模型設定視窗的標題 = 語言模型設定模塊.語言['模型設定視窗標題']
    模型設定的取消按鈕 = 語言模型設定模塊.語言['模型設定的取消按鈕']
    模型設定的儲存並關閉按鈕 = 語言模型設定模塊.語言['模型設定的儲存並離開按鈕']

    # 創建主視窗
    模型設定視窗 = tk.Tk()
    模型設定視窗.title(模型設定視窗的標題)
    模型設定視窗.resizable(False,False)
    模型視窗至中(模型設定視窗)  # 將視窗置中



    ### 讀取模型設定值 ###
    當前模型設定 = 設定模塊.讀取設定()  # 這裡會回傳 {"語言": ..., "顏色": ...}



    # global 當前ollama模型

    


    當前模型設定["ollama開關"]='false' # 這裡會回傳 "false"
    當前ollama開關 = 當前模型設定.get("ollama開關", "false")
    if 當前ollama開關 == "true":
        當前ollama開關 = True
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


    # 收尋模型模塊.url = "https://ollama.com/search?q=" + 模型單行輸入框以輸入框的值 # 設定url


    def 查詢模型(): # 查詢模型的函數
        收尋模型模塊.url = f"https://ollama.com/search?q={模型單行輸入框.get()}" # 設定url
        收尋模型模塊.爬取網頁內容(收尋模型模塊.url) # 爬取網頁內容
        url =收尋模型模塊.url # 設定url
        titles, labels = 收尋模型模塊.爬取網頁內容(url)
        查尋模型結果選單.set("") # 清空下拉選單
        查尋模型結果選單["values"] =titles # 設定下拉選單的值



        # print(模型單行輸入框以輸入框的值) # 印出單行輸入框的值
        # print(模型單行輸入框.get()) # 印出url
        # print(收尋模型模塊.url) # 印出url







    模型查詢按鈕=tk.Button(模型單行輸入框跟查詢按鈕格式,text='查詢',font=("Arial", 10),command=查詢模型) # 創建查詢按鈕
    模型查詢按鈕.place(relx=0.8,relwidth=0.2,relheight=1) # 設定大小和位置


    def 顯示已選擇的模型(event): # 當選擇模型時更新標籤的文字
        以選擇模型.config(text="選擇模型:"+查尋模型結果選單.get()) # 更新標籤的文字
        當前模型設定["查尋ollama模型結果"]=查尋模型結果選單.get()
        以選擇的查詢模型結果.set('')  # 清空當前顯示的值
        以選擇的查詢模型結果['values'] = []  # 清空下拉選單的值   

        可用版本.網址="https://ollama.com/library/" + 查尋模型結果選單.get() # 設定url
        可用版本.可用模型指令(可用版本.網址) # 爬取網頁內容
        網址=可用版本.網址 # 設定url
        可用模型參數= 可用版本.可用模型指令(網址) # 爬取網頁內容
        以選擇的查詢模型結果.delete(0, tk.END) # 清空下拉選單
        以選擇的查詢模型結果["values"] = 可用模型參數# 設定下拉選單的值




    查尋模型結果選單=ttk.Combobox(查尋模型結果選單格式,state="readonly",font=("Arial", 10)) # 創建下拉選單
    查尋模型結果選單.pack(fill=tk.X, padx=1.5, pady=1.5)    # 設定大小和位置
    查尋模型結果選單.bind("<<ComboboxSelected>>",顯示已選擇的模型) # 當選擇模型時更新標籤的文字

    def 更新以選擇的查詢模型結果(event): # 當選擇模型時更新標籤的文字
        以選擇模型.config(text="選擇模型:"+以選擇的查詢模型結果.get()) # 更新標籤的文字
  
        當前模型設定["查尋ollama模型結果"]=以選擇的查詢模型結果.get()


    以選擇的查詢模型結果=ttk.Combobox(查尋模型結果選單格式,state="readonly",font=("Arial", 10)) # 創建下拉選單
    以選擇的查詢模型結果.pack(fill=tk.X, padx=1.5, pady=1.5)    # 設定大小和位置
    以選擇的查詢模型結果.bind("<<ComboboxSelected>>",更新以選擇的查詢模型結果) # 當選擇模型時更新標籤的文字






    以選擇模型=tk.Label(以選擇模型跟詳細資訊格式,text="選擇模型:"+查尋模型結果選單.get(),font=("Arial", 11)) # 創建標籤
    以選擇模型.pack(fill=tk.X, padx=1.5, pady=0.5,side="left")  # 設定大小和位置

    以選擇模型的詳細資訊=tk.Button(以選擇模型跟詳細資訊格式,text="詳細資訊",font=("Arial", 10)) # 創建詳細資訊按鈕
    以選擇模型的詳細資訊.pack(fill=tk.X, padx=1.5, pady=1,side="right") # 設定大小和位置



































    取消和儲存並關閉按鈕=tk.Frame(模型設定視窗) # 創建一個框架來放置取消和儲存並關閉按鈕
    取消和儲存並關閉按鈕.place(relx=0.98,rely=0.98,anchor="se")     # 設定位置和大小
    # 按鈕
    取消按鈕 = tk.Button(取消和儲存並關閉按鈕, text=模型設定的取消按鈕, command=模型設定視窗.destroy)  # 創建取消按鈕
    取消按鈕.grid(column=0, row=0, sticky="ew", padx=8, pady=0.1)  # 設定大小和位置
    
    儲存並關閉按鈕 = tk.Button(取消和儲存並關閉按鈕, text=模型設定的儲存並關閉按鈕, command=更新模型設定並關閉)  # 創建儲存並關閉按鈕
    儲存並關閉按鈕.grid(column=1, row=0, sticky="ew", padx=0.1, pady=0.1)  # 設定大小和位置

    模型設定視窗.mainloop()  # 開始主循環，等待事件發生

模型設定視窗口()  # 呼叫函數以顯示視窗