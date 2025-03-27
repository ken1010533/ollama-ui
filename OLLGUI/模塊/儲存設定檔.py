import json

設定檔 = "set.json"

def 讀取設定():
    """讀取設定檔中的語言設定"""
    try:
        with open(設定檔, "r", encoding="utf-8") as f:
            return json.load(f).get("語言", "繁體中文")
    except FileNotFoundError:
        return "繁體中文"
    
def 寫入設定(語言):
    """將語言設定寫入設定檔"""
    with open(設定檔, "w", encoding="utf-8") as f:
        json.dump({"語言": 語言}, f, ensure_ascii=False, indent=4)
