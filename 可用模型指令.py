# 導入 requests 庫，用於發送 HTTP 請求
import requests
# 從 bs4 模組導入 BeautifulSoup，用於解析 HTML 文檔
from bs4 import BeautifulSoup
def 可用模型指令():
    # 設定要爬取的目標 URL
    url = "https://ollama.com/liaupal/deepseek-r1-zhenhuan"
    # 設置請求頭，模擬瀏覽器訪問（防止被網站阻擋）
    headers = {"User-Agent": "Mozilla/5.0"}

    # 發送 GET 請求獲取網頁內容
    response = requests.get(url, headers=headers)

    # 檢查 HTTP 響應狀態碼（200 表示成功）
    if response.status_code == 200:
        # 使用 BeautifulSoup 解析 HTML 內容，指定 html.parser 作為解析器
        soup = BeautifulSoup(response.text, "html.parser")
        
        # 查找 name 屬性為 "command" 的 input 標籤
        input_element = soup.find("input", {"name": "command"})
        
        # 檢查是否找到目標元素
        if input_element:
            # 獲取 input 元素的 value 屬性值
            value = input_element.get("value")
            # 輸出結果
            print("可用模型指令:", value)
        else:
            # 如果找不到元素，顯示提示信息
            print("找不到可用模型指令")
    else:
        # 如果請求失敗，顯示狀態碼
        print(f"請求失敗，狀態碼：{response.status_code}")