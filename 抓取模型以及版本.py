# 導入requests庫，用於發送HTTP請求
import requests
# 從bs4模組導入BeautifulSoup，用於解析HTML文檔
from bs4 import BeautifulSoup

# 定義要爬取的目標URL
url = "https://ollama.com/search?q=llama3.3"
# 設置請求頭偽裝成瀏覽器訪問(避免被網站封鎖)
headers = {"User-Agent": "Mozilla/5.0"}

# 發送GET請求獲取網頁內容
response = requests.get(url, headers=headers)
# 檢查HTTP響應狀態碼(200表示成功)
if response.status_code != 200:
    raise Exception(f"請求失敗，狀態碼：{response.status_code}")

# 使用BeautifulSoup解析HTML內容，指定html.parser作為解析器
soup = BeautifulSoup(response.text, "html.parser")

# 使用列表推導式提取所有<h2>標籤內的文字內容，並去除首尾空白
titles = [h2.text.strip() for h2 in soup.find_all("h2")]

# 初始化存放標籤的列表
labels = []
# 遍歷所有包含標籤的div元素(根據class屬性定位)
for div in soup.find_all("div", class_="flex flex-wrap space-x-2"):
    # 在每個div中查找所有<span>標籤，提取文字並去除首尾空白
    spans = [span.text.strip() for span in div.find_all("span")]
    # 將標籤列表轉換為字串，若無標籤則顯示"無標籤"
    labels.append(", ".join(spans) if spans else "無標籤")

# 使用zip函數配對標題和標籤，逐項輸出結果
for title, label in zip(titles, labels):
    # 格式化輸出結果，\n表示換行，f-string用於變數插入
    print(f"\n 標題: {title}  \n 標籤: {label}")