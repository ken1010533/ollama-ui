import subprocess

# 執行命令並獲取輸出
result = subprocess.run(["ls", "-l"], capture_output=True, text=True)

# 輸出內容在 result.stdout 中
print("輸出內容：")
print(result.stdout)

# 錯誤訊息在 result.stderr 中（如果有）
if result.stderr:
    print("錯誤訊息：")
    print(result.stderr)