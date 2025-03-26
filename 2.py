import requests
from bs4 import BeautifulSoup

# 設定頁面 URL
url = "https://ollama.com/library/llama3.2"
headers = {"User-Agent": "Mozilla/5.0"}

# 發送 HTTP 請求
response = requests.get(url, headers=headers)

# 檢查響應是否成功
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    
    # 查找 input 標籤，並提取 name="command" 的 value 屬性
    input_element = soup.find("input", {"name": "command"})
    
    if input_element:
        value = input_element.get("value")
        print("Command value:", value)
    else:
        print("找不到符合條件的 input 元素。")
else:
    print(f"請求失敗，狀態碼：{response.status_code}")
