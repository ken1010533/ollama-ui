
import subprocess
from tkinter import messagebox

def 檢查_ollama():

    try:
        result = subprocess.run(["where", "ollama"], capture_output=True, text=True)
        if result.returncode == 0:
            paths = result.stdout.splitlines()
            for path in paths:
                if path.endswith("ollama.exe"):
                    new_path = path.replace("ollama.exe", "ollama app.exe")
                    print("檢查結果", f"已找到 ollama.exe，並改為: {new_path}")
                    print(new_path)
                    subprocess.run('"'+new_path+'"')
                    return
            messagebox.showinfo("檢查結果", "未找到 ollama.exe ""請檢查檔案完整性\"選項---->檢查\"")
        else:
            messagebox.showerror("錯誤", "無法找到 ollama""請檢查檔案完整性\"選項---->檢查\"")
    except Exception as e:
        messagebox.showerror("錯誤", f"發生錯誤: {e}")

檢查_ollama()
 