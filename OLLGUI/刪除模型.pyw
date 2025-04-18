import requests
import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import time

伺服器位址 = "http://localhost:11434"

def 檢查服務狀態():
    try:
        回應 = requests.get(f"{伺服器位址}/api/tags", timeout=3)
        回應.raise_for_status()
        return True
    except Exception:
        return False

def 靜默啟動_ollama():
    try:
        if sys.platform.startswith("win"):
            # 在 Windows 上隱藏視窗啟動
            subprocess.Popen(
                ["ollama", "list"],
                creationflags=subprocess.CREATE_NO_WINDOW
            )
        else:
            # 在 macOS/Linux 後台執行
            subprocess.Popen(
                ["ollama", "serve"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
        time.sleep(2)  # 給它一點時間啟動
    except Exception as e:
        messagebox.showerror("啟動失敗", f"無法啟動 Ollama：\n{e}")
        exit()

def 取得模型清單():
    try:
        回應 = requests.get(f"{伺服器位址}/api/tags")
        回應.raise_for_status()
        結果 = 回應.json()
        return [模型["name"] for 模型 in 結果.get("models", [])]
    except Exception as e:
        messagebox.showerror("錯誤", f"❌ 發生錯誤（取得模型清單）:\n{e}")
        return []

def 刪除模型(模型名稱):
    try:
        回應 = requests.delete(f"{伺服器位址}/api/delete", json={"name": 模型名稱})
        回應.raise_for_status()
    except Exception as e:
        messagebox.showerror("錯誤", f"❌ 刪除請求發生錯誤:\n{e}")
        return

    模型清單 = 取得模型清單()
    if 模型名稱 not in 模型清單:
        messagebox.showinfo("成功", f"✅ 模型『{模型名稱}』刪除成功！")
        更新模型清單()
    else:
        messagebox.showwarning("警告", f"⚠️ 模型『{模型名稱}』仍存在，刪除可能失敗。")

def 更新模型清單():
    模型清單 = 取得模型清單()
    清單框.delete(0, tk.END)
    for 模型 in 模型清單:
        清單框.insert(tk.END, 模型)

def 刪除選取模型():
    選取 = 清單框.curselection()
    if not 選取:
        messagebox.showwarning("提醒", "⚠️ 請先選取要刪除的模型。")
        return
    模型名稱 = 清單框.get(選取[0])
    刪除模型(模型名稱)

# 啟動時靜默確認並啟動服務
if not 檢查服務狀態():
    靜默啟動_ollama()
    for _ in range(5):  # 最多等 5 秒讓服務啟動
        if 檢查服務狀態():
            break
        time.sleep(1)
    else:
        messagebox.showerror("錯誤", "Ollama 無法啟動或連線失敗。")
        exit()

# GUI 開始
視窗 = tk.Tk()
視窗.title("🧹 Ollama 模型刪除工具")

提示標籤 = tk.Label(視窗, text="📦 目前的模型：")
提示標籤.pack(pady=(10, 0))

清單框 = tk.Listbox(視窗, width=50)
清單框.pack(pady=5)

刪除按鈕 = tk.Button(視窗, text="刪除選取模型", command=刪除選取模型)
刪除按鈕.pack(pady=10)

更新模型清單()
視窗.mainloop()
