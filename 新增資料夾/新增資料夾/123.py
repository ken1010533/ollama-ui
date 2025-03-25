import subprocess

# 開啟 VS Code 終端機 (PowerShell)
process = subprocess.Popen(
    ["powershell.exe"],  # 這裡可以改成 "cmd.exe" 或 "bash" 依需求
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
    bufsize=1  # 讓輸出即時顯示
)

# 持續監聽 VS Code 終端機的輸出
while True:
    output = process.stdout.readline()
    if output:
        print("終端機輸出:", output.strip())  # 監聽並打印 VS Code 終端機的輸出
