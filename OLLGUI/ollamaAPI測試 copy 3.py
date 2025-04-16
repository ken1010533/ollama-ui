import requests

class 測試對話模型:
    def __init__(self, 模型名稱="llama3", 伺服器="http://localhost:11434"):
        self.模型名稱 = 模型名稱
        self.伺服器 = 伺服器
        self.對話歷史 = []

    def 發送(self, 使用者輸入):
        # 將對話歷史整理為一段 prompt
        prompt = ""
        for msg in self.對話歷史:
            prefix = "你：" if msg["role"] == "user" else "AI："
            prompt += f"{prefix}{msg['content']}\n"
        prompt += f"你：{使用者輸入}\nAI："

        請求內容 = {
            "model": self.模型名稱,
            "prompt": prompt,
            "stream": False
        }

        try:
            回應 = requests.post(f"{self.伺服器}/api/generate", json=請求內容)
            回應.raise_for_status()
            結果 = 回應.json()

            回覆 = 結果.get("response", "⚠️ 沒有回傳內容")
            self.對話歷史.append({"role": "user", "content": 使用者輸入})
            self.對話歷史.append({"role": "assistant", "content": 回覆})
            return 回覆
        except Exception as 錯誤:
            return f"❌ 發送失敗：{錯誤}"

    def 清除對話(self):
        self.對話歷史 = []

# ========== 測試入口 ==========
if __name__ == "__main__":
    模型 = 測試對話模型("llama3")

    print("💬 模型聊天測試開始（輸入 exit 離開）")
    while True:
        使用者輸入 = input("你：")
        if 使用者輸入.lower() in ["exit", "quit", "離開"]:
            print("👋 結束測試。")
            break

        回覆 = 模型.發送(使用者輸入)
        print("🤖：", 回覆)
