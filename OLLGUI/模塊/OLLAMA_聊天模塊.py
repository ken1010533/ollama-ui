import requests

class 模型對話器:
    def __init__(self, 模型名稱="llama3", 伺服器位址="http://localhost:11434"):
        self.伺服器 = 伺服器位址
        self.模型名稱 = 模型名稱
        self.對話歷史 = []

    def 發送訊息(self, 使用者訊息):
        if not 使用者訊息.strip():
            print("錯誤: 輸入訊息為空")
            return "訊息內容不可為空，請重新輸入。"

        路徑 = f"{self.伺服器}/api/chat"
        資料 = {
            "模型": self.模型名稱,

            "訊息": [{"角色": "使用者", "內容": 使用者訊息}],

            "對話": self.對話歷史
            
        }

        # 將中文參數轉換為 Ollama API 規定的英文欄位
        轉換資料 = {
            "model": 資料["模型"],
            "messages": [
                {"role": m["角色"], "content": m["內容"]} for m in 資料["訊息"]
            ] + self.對話歷史
        }

        try:
            回應 = requests.post(路徑, json=轉換資料)
            回應.raise_for_status()  # 確保 HTTP 狀態碼是 200 OK

            結果 = 回應.json()

            # Debug 輸出，檢查回應的實際內容
            print("API 回應:", 結果)

            # 檢查結果結構是否正確
            if "message" in 結果 and "content" in 結果["message"]:
                機器人回覆 = 結果["message"]["content"]
                self.對話歷史.append({"role": "user", "content": 使用者訊息})
                self.對話歷史.append({"role": "assistant", "content": 機器人回覆})
                return 機器人回覆
            else:
                print("錯誤: API 回應結構不符合預期。")
                return "無法處理請求，請再試一次。"

        except requests.exceptions.RequestException as e:
            print(f"網絡或請求錯誤: {e}")
            return "發生錯誤，請檢查網絡連接或伺服器狀態。"
        except ValueError as e:
            print(f"無效的 JSON 回應: {e}")
            return "伺服器回應無效，請稍後再試。"



    def 重置對話(self):
        self.對話歷史 = []
