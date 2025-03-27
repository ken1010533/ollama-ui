# 導入requests庫，用於發送HTTP請求
import requests
# 從bs4模組導入BeautifulSoup，用於解析HTML文檔
from bs4 import BeautifulSoup
  
# 定義要爬取的目標URL（Ollama模型庫中的llama3.1頁面）
url = "https://ollama.com/library/gemma3"

# 設置請求頭偽裝成瀏覽器訪問（使用Chrome瀏覽器的User-Agent）
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

# 發送GET請求獲取網頁內容
response = requests.get(url, headers=headers)

# 檢查HTTP響應狀態碼（200表示成功）
if response.status_code == 200:
    # 使用BeautifulSoup解析HTML內容，指定html.parser作為解析器
    soup = BeautifulSoup(response.text, "html.parser")
    
    # 使用CSS選擇器查找id="display"元素內的所有<pre>標籤
    # 說明：這裡假設代碼內容是放在<pre>標籤中，且位於id="display"的容器內
    pre_tags = soup.select("#display pre")
    
    # 檢查是否找到<pre>標籤
    if not pre_tags:
        print("未找到代碼內容（沒有<pre>標籤）嘗試找可用模型指令")
        #可用模型指令.可用模型指令()


        if response.status_code == 200:
            # 使用 BeautifulSoup 解析 HTML 內容，指定 html.parser 作為解析器
            soup = BeautifulSoup(response.text, "html.parser")
            
            # 查找 name 屬性為 "command" 的 input 標籤
            input_element = soup.find("input", {"name": "command"})
            
            # 檢查是否找到目標元素
            if input_element:
                # 獲取 input 元素的 value 屬性值
                value = input_element.get("value") # type: ignore
                # 輸出結果
                print("可用模型指令:", value)
            else:
                # 如果找不到元素，顯示提示信息
                print("找不到可用模型指令")
        else:
            # 如果請求失敗，顯示狀態碼
            print(f"請求失敗，狀態碼：{response.status_code}")
    else:
        # 迭代所有找到的<pre>標籤
        for i, pre in enumerate(pre_tags):
            # 打印每個<pre>標籤的內容，並用strip()去除首尾空白
            print(f"\n 可用模型指令:\n{pre.text.strip()}")
else:
    # 如果請求失敗，打印錯誤狀態碼
    print(f"請求失敗，狀態碼：{response.status_code}")
    # 建議：可以根據不同狀態碼提供更具體的反饋信息，例如404表示頁面不存在