import requests
import json

class 串流對話模型:
    def __init__(self, 模型名稱, 伺服器="http://localhost:11434"):
        self.伺服器 = 伺服器
        self.模型名稱 = 模型名稱
        self.對話歷史 = []

    def 發送(self, 使用者輸入):
        prompt = ""
        for msg in self.對話歷史:
            prefix = "你：" if msg["role"] == "user" else "AI:"
            prompt += f"{prefix}{msg['content']}\n"
        prompt += f"你：{使用者輸入}\nAI:"

        請求內容 = {
            "model": self.模型名稱,
            "prompt": prompt,
            "stream": True
        }

        try:
            回應 = requests.post(f"{self.伺服器}/api/generate", json=請求內容, stream=True)
            回應.raise_for_status()

            print("🤖：", end="", flush=True)
            回覆內容 = ""
            for 行 in 回應.iter_lines():
                if 行:
                    資料 = json.loads(行.decode("utf-8"))
                    token = 資料.get("response", "")
                    print(token, end="", flush=True)
                    回覆內容 += token

            print()
            self.對話歷史.append({"role": "user", "content": 使用者輸入})
            self.對話歷史.append({"role": "assistant", "content": 回覆內容})

        except Exception as 錯誤:
            print(f"\n❌ 發送失敗：{錯誤}")

    def 清除對話(self):
        self.對話歷史 = []

def 取得模型清單(伺服器="http://localhost:11434"):
    try:
        r = requests.get(f"{伺服器}/api/tags")
        r.raise_for_status()
        return [m["name"] for m in r.json().get("models", [])]
    except Exception as e:
        print(f"❌ 無法取得模型清單：{e}")
        return []

def 選擇模型(伺服器="http://localhost:11434"):
    模型們 = 取得模型清單(伺服器)
    if not 模型們:
        print("📭 沒有可用模型，請先拉取模型。")
        return None

    print("📦 可用模型：")
    for i, m in enumerate(模型們, 1):
        print(f"{i}. {m}")

    while True:
        try:
            選 = int(input("🔢 請輸入模型編號："))
            if 1 <= 選 <= len(模型們):
                return 模型們[選 - 1]
            else:
                pass
        except  Exception as e:
            print(f"⚠️ 輸入錯誤：{e}，請輸入整數。")
            print("⚠️ 請輸入整數。")

# 🏁 主程式
if __name__ == "__main__":
    模型名 = 選擇模型()
    if 模型名:
        模型 = 串流對話模型(模型名)

        print("💬 開始聊天！(輸入 `exit` 離開，`clear` 清除對話，`switch` 換模型)\n")
        while True:
            使用者輸入 = input("你：")
            if 使用者輸入.lower() in ["exit", "quit", "離開"]:
                print("👋 再見！")
                break
            elif 使用者輸入.lower() == "clear":
                模型.清除對話()
                print("🧹 已清除對話歷史。\n")
            elif 使用者輸入.lower() == "switch":
                模型名 = 選擇模型()
                if 模型名:
                    模型 = 串流對話模型(模型名)
                    print(f"🔁 已切換至模型：{模型名}\n")
            else:
                模型.發送(使用者輸入)
