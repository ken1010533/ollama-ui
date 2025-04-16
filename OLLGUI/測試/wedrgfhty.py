import requests

while True:
    entry_id = input("請輸入數字 ID: ")
    if entry_id.isdigit():
        url = "https://sg-wiki-api-static.hoyolab.com/hoyowiki/genshin/wapi/entry_page?entry_page_id=" + entry_id
        break
    else:
        print("輸入無效，請輸入數字。")

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Origin": "https://wiki.hoyolab.com",
    "Referer": "https://wiki.hoyolab.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    "x-rpc-language": "zh-tw",
    "x-rpc-wiki_app": "genshin",
}

response = requests.get(url, headers=headers)

print("狀態碼:", response.status_code)

try:
    data = response.json()
    print("名稱:", data.get("data", {}).get("page", {}).get("name"))
    # print("回傳資料內容:")
    print(data)
    
    # 整理資料部分
    print("\n===== 整理後的武器資料 =====")
    page_data = data.get("data", {}).get("page", {})
    
    # 基本資訊
    print("\n【基本資訊】")
    print(f"名稱: {page_data.get('name')}")
    print(f"類型: {page_data.get('filter_values', {}).get('weapon_type', {}).get('values', [''])[0]}")
    print(f"稀有度: {page_data.get('filter_values', {}).get('weapon_rarity', {}).get('values', [''])[0]}")
    print(f"副屬性: {page_data.get('filter_values', {}).get('weapon_property', {}).get('values', [''])[0]}")
    print(f"描述: {page_data.get('desc', '')}")
    
    # 武器效果
# 武器效果
    modules = page_data.get('modules', [])
    for module in modules:
        if module.get('name') == '屬性':
            components = module.get('components', [])
            for comp in components:
                if comp.get('component_id') == 'baseInfo':
                    base_info = comp.get('data', '{}')
                    import json
                    try:
                        base_info = json.loads(base_info)
                        print("\n【武器效果】")
                        for item in base_info.get('list', []):
                            # 移除 HTML 標籤
                            import re
                            effect_name = item.get('key', '')
                            effect_text = item.get('value', [''])[0]
                            clean_text = re.sub(r'<[^>]+>', '', effect_text)
                            print(f"{effect_name}: {clean_text}")
                    except Exception as e:
                        print(f"Error processing baseInfo: {e}")
    
except Exception as e:
    print("解析 JSON 失敗:", e)
    print("原始內容:", response.text)
