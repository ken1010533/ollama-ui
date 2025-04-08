from pathlib import Path # 文件路径库
import re

# 定义语言代码的正则表达式（如 en_US, zh_CN, ja_JP）
LANG_CODE_PATTERN = re.compile(r"^[a-z]{2}(-[A-Z]{2})?$")  # 语言代码格式正则表达式

# 假设语言文件夹名称是 "語言資料" 或 "locales"
language_dir = Path.cwd() / "語言"  # 替换成你的实际文件夹名

if language_dir.exists() and language_dir.is_dir(): # 检查文件夹是否存在
    subfolders = [ # 获取所有符合语言代码格式的子文件夹
        folder.name for folder in language_dir.iterdir()   # 遍历文件夹
        if folder.is_dir() and LANG_CODE_PATTERN.match(folder.name) # 检查是否为文件夹和是否符合语言代码格式
    ]
    
    #print("符合語言代碼格式的子資料夾：") # 输出符合语言代码格式的子文件夹
    for folder in subfolders:  # 遍历子文件夹
        #print(folder) # 输出子文件夹名称
        語言翻譯=subfolders # 獲取語言翻譯
else:   # 如果文件夹不存在
    print(f"'{language_dir}' 資料夾不存在！")   # 输出文件夹不存在的信息