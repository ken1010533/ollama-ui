import requests
from bs4 import BeautifulSoup

# 設定 URL
url = "https://ollama.com/library/llama3.1"

# 設定 User-Agent，避免網站識別為機器人
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# 發送 GET 請求
response = requests.get(url, headers=headers)

# 確保請求成功
if response.status_code == 200:
    # 解析 HTML 內容
    soup = BeautifulSoup(response.text, "html.parser")
    
    # 查找所有 <pre> 標籤
    pre_tags = soup.select("#display pre")  # 使用 CSS 選擇器選擇 id="display" 中的所有 <pre> 標籤
    
    # 迭代並打印每個 <pre> 標籤的內容
    for pre in pre_tags:
        print(pre.text.strip())  # 使用 strip() 去掉多餘的空白
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
