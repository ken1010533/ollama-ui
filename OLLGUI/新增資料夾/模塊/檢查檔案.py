import subprocess   #執行系統
from tkinter import messagebox #引入訊息視窗函式庫
import webbrowser #引入瀏覽器函式庫

def 檢查檔案():
    try:    #變數名稱  #執行系統   執行   ollama -version        #跟執行系統抓取輸出#格式是文字          
        檢查ollama版本=subprocess.run(["ollama","--version"],capture_output=True,text=True)#檢查ollama是否安裝跟版本
        if 檢查ollama版本.returncode == 0: #如果檢查ollama版本回傳碼是0
            return True #回傳True
    except Exception: #如果有錯誤或是沒安裝
        return False #回傳False
if 檢查檔案(): #如果檢查檔案
    subprocess.Popen("ollama serve", shell=True) #執行ollama serve
else:
    if messagebox.askyesno("未安裝 ollama", "您未安裝 ollama，是否前往安裝？"): #如果訊息視窗問是否要安裝
        webbrowser.open("https://ollama.com/")# 開啟網頁
