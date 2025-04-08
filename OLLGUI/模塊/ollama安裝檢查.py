#region

# 宣告使用的函式庫
#import ctypes
import subprocess   #執行系統
from tkinter import messagebox #引入訊息視窗函式庫
import webbrowser #引入瀏覽器函式庫




def 檢查_ollama_是否安裝():
    """
    檢查_ollama_是否安裝()
    檢查是否已安裝 ollama 命令行工具。
    Returns:
        bool: 如果 ollama 已安裝，返回 True，否則返回 False。
    Raises:
        Exception: 如果在檢查過程中發生任何異常，捕獲並返回 False。
    """
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


def 檢查_ollama_版本():
    try:
        # 假設這裡是檢查 ollama 是否安裝的邏輯
        result = subprocess.run(["ollama", "--version"], capture_output=True, text=True)
        messagebox.showinfo("檢查結果", f"ollama 已安裝，版本: {result.stdout}")
        
    except Exception as e:
        messagebox.showerror("錯誤", f"發生錯誤: {e}")

def 關閉_ollama():
    """
    關閉 ollama 服務
    """
    try:
        subprocess.Popen('taskkill /IM "ollama.exe" /F', shell=True)
        subprocess.Popen('taskkill /IM "ollama app.exe" /F', shell=True)
        messagebox.showinfo("關閉 ollama", "ollama 已關閉")
    except Exception as e:
        messagebox.showerror("錯誤", f"發生錯誤: {e}")


'''

if not ollama安裝檢查.檢查_ollama_是否安裝():
    messagebox.showerror("錯誤", "請檢查檔案完整性\"選項---->檢查\"")
    root.destroy()
    '''