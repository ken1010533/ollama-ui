import requests
from bs4 import BeautifulSoup

def 搜尋模組版本(模型版本網址):
    回應 = requests.get(模型版本網址)
    解析 = BeautifulSoup(回應.text, 'html.parser')
    模型區塊列表 = 解析.select('div.flex.px-4.py-3')

    計數 = 0
    結果 = []
    for 模型區塊 in 模型區塊列表:
        名稱元素 = 模型區塊.select_one('a.group div')
        if not 名稱元素 or not 名稱元素.text.strip():
            continue  # 跳過空白項目

        編號元素 = 模型區塊.select_one('span.font-mono')
        資訊元素 = 模型區塊.select_one('div.flex.items-baseline span')

        名稱 = 名稱元素.text.strip()
        模型編號 = 編號元素.text.strip() if 編號元素 else ""
        原始資訊 = 資訊元素.text.strip() if 資訊元素 else ""

        資訊片段 = [段.strip() for 段 in 原始資訊.split('•') if 段.strip()]
        容量 = 資訊片段[1] if len(資訊片段) > 1 else ""
        發佈時間 = 資訊片段[2] if len(資訊片段) > 2 else ""
        

        # print(f"模型名稱：{名稱}")
        # print(f"模型編號：{模型編號}")
        # print(f"模型容量：{容量}")
        # print(f"發佈時間：{發佈時間}")
        # print("--------")

        計數 += 1
        結果.append((名稱, 模型編號, 容量, 發佈時間))
    

    # print(f"目前共找到 {計數} 筆模型版本資料")
    # print("--------")
    # print(模型版本網址)
    return 結果, 計數, 模型版本網址

模型名稱 =None
if 模型名稱 is None:
    模型名稱 = "llama2"
def 預設模型(模型名稱):
    模型版本網址 = f"https://ollama.com/library/{模型名稱}/tags"
    return 搜尋模組版本(模型版本網址)
# 搜尋模組版本(模型版本網址)
