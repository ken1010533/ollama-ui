import requests

def 取模型列表(伺服器位址="http://localhost:11434"):
    路徑 = f"{伺服器位址}/api/tags"
    try:
        回應 = requests.get(路徑)
        回應.raise_for_status()
        結果 = 回應.json()

        # 顯示模型清單
        模型清單 = 結果.get("models", [])
        for 模型 in 模型清單:
            print(f"模型名稱: {模型['name']}")
            print(f"摘要 (digest): {模型['digest']}")
            def 格式化大小(byte數):
                mb = byte數 / 1024 / 1024
                if mb < 1024:
                    return f"{mb:.2f} MB"
                else:
                    gb = mb / 1024
                    return f"{gb:.2f} GB"

            print(f"大小: {格式化大小(模型['size'])}")
            print(f"修改時間: {模型['modified_at']}")
            print("-" * 30)
    except Exception as e:
        print(f"發生錯誤：{e}")

# 呼叫函式
取模型列表()
