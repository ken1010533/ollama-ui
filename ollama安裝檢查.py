#region

# 宣告使用的函式庫
#import ctypes
import subprocess
from tkinter import messagebox
import webbrowser




def 檢查_ollama_是否安裝():
    try:
        result = subprocess.run(["ollama","--version"], capture_output=True, text=True)

        if result.returncode == 0:
            return True
    except Exception:

        return False

if 檢查_ollama_是否安裝():
    subprocess.Popen("ollama serve", shell=True)

else:
    if messagebox.askyesno("未安裝 ollama", "您未安裝 ollama，是否前往安裝？"):
        webbrowser.open("https://ollama.com/")