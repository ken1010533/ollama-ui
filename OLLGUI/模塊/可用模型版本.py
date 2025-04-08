# 導入requests庫，用於發送HTTP請求
import requests
# 從bs4模組導入BeautifulSoup，用於解析HTML文檔
from bs4 import BeautifulSoup
# 定義要爬取的目標網址（Ollama模型庫中的llama3.1頁面）
網址 = None
if 網址 is None:  
    # 如果網址為None，則從用戶輸入獲取網址
    網址 = "https://ollama.com/library/"
def 可用模型指令(url=網址):  # 定義函數以獲取可用模型指令
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}  # 設定請求頭，模擬瀏覽器行為
    response = requests.get(url, headers=headers)  # 發送GET請求獲取網頁內容
    
    可用模型參數 = []  # 初始化為空列表
    
    if response.status_code == 200:  # 如果請求成功
        soup = BeautifulSoup(response.text, "html.parser")  # 解析HTML文檔
        pre_tags = soup.select("#display pre")  # 使用CSS選擇器查找所有pre標籤
        
        if pre_tags:
            for pre in pre_tags:
                可用模型參數.append(pre.text.strip())  # 追加到列表
            print(f"找到的模型指令: {可用模型參數}")  # 輸出找到的指令 
        else:
            print("嘗試查找其他格式的指令...")  # 如果沒有找到pre標籤，則嘗試查找其他格式的指令 
            input_elements = soup.find_all("input", {"name": "command"})  # 查找所有input元素
            for input_element in input_elements:  # 查找所有input元素 
                if input_element.has_attr("value"):  # 檢查是否有value屬性
                    可用模型參數.append(input_element["value"])  # 追加到列表
            
            if not 可用模型參數:  # 如果仍然沒有找到指令
                print("找不到任何可用指令")  # 如果仍然找不到指令，則輸出提示信息
                return [""]  # 返回一個預設值避免空列表
    else:
        print(f"請求失敗，狀態碼：{response.status_code}")  # 輸出錯誤狀態碼
        return [""]  # 返回錯誤信息
    
    return 可用模型參數  # 返回所有找到的指令
可用模型指令()  # 呼叫函數以獲取可用模型指令