import json

設定檔 = "set.json"

def 讀取設定():
    """讀取設定檔中的語言設定"""
    try: # 嘗試讀取設定檔
        with open(設定檔, "r", encoding="utf-8") as f: # 使用 utf-8 編碼讀取設定檔
            return json.load(f).get("語言", "繁體中文") # 預設為繁體中文
    except FileNotFoundError: # 如果設定檔不存在，則返回預設語言
        return "繁體中文" # 預設為繁體中文
    
    
def 寫入設定(語言): # 將語言設定寫入設定檔
    """將語言設定寫入設定檔""" 
    with open(設定檔, "w", encoding="utf-8") as f: # 使用 utf-8 編碼寫入設定檔
        json.dump({"語言": 語言}, f, ensure_ascii=False, indent=4) # 將語言設定寫入設定檔
