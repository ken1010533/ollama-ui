import requests
import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import time

if __name__ == "__main__":
    import 語言設定模塊 as 語言模型設定模塊
    from 視窗至中模塊 import 模型視窗至中
    from 單一視窗模塊 import 單一視窗
else:
    from 模塊 import 語言設定模塊 as 語言模型設定模塊
    from 模塊.視窗至中模塊 import 模型視窗至中
    from 模塊.單一視窗模塊 import 單一視窗

# ========= 刪除模型邏輯 =========
刪除頁面視口 = None
伺服器位址 = "http://localhost:11434"
def 刪除頁面視窗():
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
                subprocess.Popen(["ollama", "list"], creationflags=subprocess.CREATE_NO_WINDOW)
            else:
                subprocess.Popen(["ollama", "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            time.sleep(2)
        except Exception as e:
            messagebox.showerror(語言模型設定模塊.語言['刪除視窗']['啟動失敗'],
                                f"{語言模型設定模塊.語言['刪除視窗']['無法啟動Ollama']}\n{e}")
            exit()

    def 取得模型清單():
        try:
            回應 = requests.get(f"{伺服器位址}/api/tags")
            回應.raise_for_status()
            結果 = 回應.json()
            return [模型["name"] for 模型 in 結果.get("models", [])]
        except Exception as e:
            messagebox.showerror(語言模型設定模塊.語言['刪除視窗']['錯誤'],
                                f"❌ {語言模型設定模塊.語言['刪除視窗']['發生錯誤（取得模型清單）']}:\n{e}")
            return []

    def 刪除模型(模型名稱, 清單框):
        try:
            requests.delete(f"{伺服器位址}/api/delete", json={"name": 模型名稱}).raise_for_status()
        except Exception as e:
            messagebox.showerror(語言模型設定模塊.語言['刪除視窗']['錯誤'],
                                f"❌ {語言模型設定模塊.語言['刪除視窗']['刪除請求發生錯誤']}:\n{e}")
            return

        模型清單 = 取得模型清單()
        if 模型名稱 not in 模型清單:
            messagebox.showinfo(語言模型設定模塊.語言['刪除視窗']['成功'],
                                f"{語言模型設定模塊.語言['刪除視窗']['模型']}{模型名稱}{語言模型設定模塊.語言['刪除視窗']['刪除成功']}!")
        else:
            messagebox.showwarning(語言模型設定模塊.語言['刪除視窗']['警告'],
                                f"{語言模型設定模塊.語言['刪除視窗']['模型']}{模型名稱}{語言模型設定模塊.語言['刪除視窗']['仍存在刪除可能失敗']}")

        更新模型清單(清單框)

    def 更新模型清單(清單框):
        模型清單 = 取得模型清單()
        清單框.delete(0, tk.END)
        for 模型 in 模型清單:
            清單框.insert(tk.END, 模型)

    def 刪除選取模型(清單框):
        選取 = 清單框.curselection()
        if not 選取:
            messagebox.showwarning(語言模型設定模塊.語言['刪除視窗']['提醒'],
                                語言模型設定模塊.語言['刪除視窗']['請先選取要刪除的模型'])
            return
        模型名稱 = 清單框.get(選取[0])
        確認訊息 = 語言模型設定模塊.語言['刪除視窗']['是否確定要刪除模型{模型名稱}'].format(模型名稱=模型名稱)
        確認 = messagebox.askyesno(語言模型設定模塊.語言['刪除視窗']['警告'], 確認訊息)
        if 確認:
            刪除模型(模型名稱, 清單框)

    # ========= 單一視窗包裝器 =========

    def 顯示刪除視窗(父視窗):
        視窗控制 = 單一視窗(父視窗, 標題=語言模型設定模塊.語言['刪除視窗']['刪除視窗標題'])

        def 建立內容(視窗):
            模型視窗至中(視窗)

            提示標籤 = tk.Label(視窗, text=語言模型設定模塊.語言['刪除視窗']['目前的模型'])
            提示標籤.pack(pady=(10, 0))

            清單框 = tk.Listbox(視窗, width=50)
            清單框.pack(pady=5)

            刪除按鈕 = tk.Button(
                視窗,
                text=語言模型設定模塊.語言['刪除視窗']['刪除選取模型文字'],
                command=lambda: 刪除選取模型(清單框)
            )
            刪除按鈕.pack(pady=10)

            更新模型清單(清單框)

        # 啟動服務（若未啟動）
        if not 檢查服務狀態():
            靜默啟動_ollama()
            for _ in range(5):
                if 檢查服務狀態():
                    break
                time.sleep(1)
            else:
                messagebox.showerror(語言模型設定模塊.語言['刪除視窗']['錯誤'],
                                    語言模型設定模塊.語言['刪除視窗']['Ollama無法啟動或連線失敗'])
                return

        視窗控制.顯示(建立內容)

    # ========= 主測試程式（可選） =========

    global 刪除頁面視口
    if 刪除頁面視口 is None or not 刪除頁面視口.winfo_exists():
        刪除頁面視口= tk.Tk()
        刪除頁面視口.title("Ollama 管理工具")

        開啟按鈕 = tk.Button(刪除頁面視口, text="開啟刪除視窗", command=lambda: 顯示刪除視窗(刪除頁面視口))
        開啟按鈕.pack(padx=20, pady=20)

        刪除頁面視口.mainloop()