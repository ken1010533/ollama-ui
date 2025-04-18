import requests
from bs4 import BeautifulSoup  # type: ignore

網址 = None  # 網址預設為None，會自動使用預設網址
if 網址 is None:
    網址 = "https://ollama.com/search?q="  # 預設網址
# 輸入內容 = None  # 輸入內容預設為None，會自動使用預設內容
# if 輸入內容 is None:
#     輸入內容 = 網址  # 直接使用網址

def 爬取網頁內容(網址):  # 定義一個函數來爬取網頁內容
    請求頭 = {"User-Agent": "Mozilla/5.0"}  # 設定請求頭，模擬瀏覽器行為
    try:
        回應 = requests.get(網址, headers=請求頭)  # 發送請求，獲取網頁內容
        回應.raise_for_status()  # 如果狀態碼不是200，會自動拋出異常
    except requests.RequestException as e:
        raise Exception(f"請求失敗: {e}")  # 捕獲並顯示異常

    解析器 = BeautifulSoup(回應.text, "html.parser")  # 使用BeautifulSoup解析網頁內容
    標題列表 = [h2.text.strip() for h2 in 解析器.find_all("h2")]  # type: ignore
    標籤列表 = []  # 初始化標籤列表
    for div in 解析器.find_all("div", class_="flex flex-wrap space-x-2"):  # type: ignore
        spans = [span.text.strip() for span in div.find_all("span")]  # type: ignore
        標籤列表.append(", ".join(spans) if spans else "無標籤")  # 如果沒有標籤，則設為"無標籤"

    # 輸出每條資料的標題與標籤
    for 標題, 標籤 in zip(標題列表, 標籤列表):  # 將標題和標籤配對
        print(f"\n 標題: {標題}  \n 標籤: {標籤}")  # type: ignore
    
    # 計算資料筆數
    資料筆數 = len(標題列表)
    print(f"\n總共抓取了 {資料筆數} 筆資料。")  # 輸出資料筆數
    
    return 標題列表, 標籤列表, 資料筆數  # 返回標題、標籤列表和資料筆數

# 呼叫函數，爬取網頁內容
# 爬取網頁內容(輸入內容)
