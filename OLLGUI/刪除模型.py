import requests

伺服器位址 = "http://localhost:11434"

def 取得模型清單():
    try:
        回應 = requests.get(f"{伺服器位址}/api/tags")
        回應.raise_for_status()
        結果 = 回應.json()
        return [模型["name"] for 模型 in 結果.get("models", [])]
    except Exception as e:
        print(f"❌ 發生錯誤（取得模型清單）: {e}")
        return []

def 刪除模型(模型名稱):
    try:
        回應 = requests.delete(f"{伺服器位址}/api/delete", json={"name": 模型名稱})
        回應.raise_for_status()
    except Exception as e:
        print(f"❌ 刪除請求發生錯誤: {e}")
        return

    # 再次查詢確認模型是否還存在
    模型清單 = 取得模型清單()
    if 模型名稱 not in 模型清單:
        print(f"✅ 模型『{模型名稱}』刪除成功！")
    else:
        print(f"⚠️ 模型『{模型名稱}』仍存在，刪除可能失敗。")

def 選擇並刪除模型():
    模型清單 = 取得模型清單()
    if not 模型清單:
        print("📭 沒有可用的模型。")
        return

    print("📦 目前的模型：")
    for idx, 模型 in enumerate(模型清單, start=1):
        print(f"{idx}. {模型}")

    try:
        選擇 = int(input("請輸入要刪除的模型編號："))
        if 1 <= 選擇 <= len(模型清單):
            刪除模型(模型清單[選擇 - 1])
        else:
            print("⚠️ 無效的編號。")
    except ValueError:
        print("⚠️ 請輸入有效的整數。")

# 🏁 執行
選擇並刪除模型()
