import requests
from urllib.parse import quote

url = "https://sg-wiki-api.hoyolab.com/hoyowiki/genshin/wapi/get_entry_page_list"

# 設定 Headers，包含多個 cookie，使用分號隔開
headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://wiki.hoyolab.com/",
    "Origin": "https://wiki.hoyolab.com",
    "Cookie":quote("ltoken_v2=v2_CAISDGN3a2o5dno3cGNzZxokYjQ1MGNhYTctMjRhZC00ODBhLTg2NmMtYTQwYTlmMzViNzc1IKbr4r8GKK7Mks0EMN7u-mFCC2Jic19vdmVyc2Vh.prX4ZwAAAAAB.MEYCIQDhOXj68xZdoNjXOuQnBQhqDHvcJrwF-g9bDh9LiftYXwIhAKyqlWSL46aDNwG_nwrceIAClD8-GFW5UuejN-73bKJa; mi18nLang=zh-tw")
}

# 設定 POST 傳送的資料（這邊 menu_id: 5 是聖遺物，可依需求調整）
data = {
    "filters": [],
    "menu_id": "4",  # 聖遺物頁面
    "page_num": 1,
    "page_size": 1,
    "use_es": True,
    "lang": "zh-tw"
}

# 發送請求
response = requests.post(url, json=data, headers=headers)

# 印出狀態碼與回應內容
print("狀態碼:", response.status_code)

try:
    print("回應內容:", response.json())
except Exception as e:
    print("解析 JSON 失敗:", e)
    print("原始回應:", response.text)
