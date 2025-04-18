import requests
import sys
import 模塊.儲存設定檔 as 設定檔
# 模型名稱 = 設定檔.讀取設定("模型名稱")
def 拉取模型(模型名稱, 伺服器位址="http://localhost:11434"):
    路徑 = f"{伺服器位址}/api/pull"
    請求資料 = {"name": 模型名稱}

    try:
        回應 = requests.post(路徑, json=請求資料, stream=True)
        回應.raise_for_status()

        for 行 in 回應.iter_lines():
            if 行:
                行文字 = 行.decode("utf-8")
                try:
                    資料 = eval(行文字.replace("true", "True").replace("false", "False"))
                    if "status" in 資料:
                        狀態 = 資料["status"]
                        百分比 = ""

                        if "total" in 資料 and "completed" in 資料:
                            total = 資料["total"]
                            done = 資料["completed"]
                            ratio = done / total
                            bar_len = 30
                            filled_len = int(bar_len * ratio)
                            bar = "█" * filled_len + "░" * (bar_len - filled_len)
                            百分比 = f" [{bar}] {int(ratio * 100)}%"

                        print(f"\r→ {狀態}{百分比}", end="")
                        sys.stdout.flush()
                    elif "error" in 資料:
                        print(f"\n❌ 錯誤: {資料['error']}")
                        break
                except Exception as e:
                    print(f"\n⚠️ 解析錯誤: {e}")
                    print(f"原始資料: {行文字}")
                    break

        print("\n✅ 模型拉取完成")
    except Exception as e:
        print(f"❌ 發生錯誤: {e}")

# 測試用
if __name__ == "__main__":
    模型名稱 = "deepseek-r1:14b"
    拉取模型(模型名稱)
