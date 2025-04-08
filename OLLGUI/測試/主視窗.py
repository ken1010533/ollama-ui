import tkinter as tk
from 模型視a窗 import 模型設定視窗口
from 設定視窗a import 設定視窗口
from 參數輸出視窗 import 顯示參數結果

def 建立主選單():
    主視窗 = tk.Tk()
    主視窗.title("Ollama GPT 工具")
    主視窗.geometry("300x250")
    主視窗.resizable(False, False)

    標題 = tk.Label(主視窗, text="請選擇要執行的設定", font=("Arial", 14))
    標題.pack(pady=20)

    tk.Button(主視窗, text="模型設定", font=("Arial", 12), width=20, command=模型設定視窗口).pack(pady=5)
    tk.Button(主視窗, text="其他設定", font=("Arial", 12), width=20, command=設定視窗口).pack(pady=5)
    tk.Button(主視窗, text="參數輸出監控", font=("Arial", 12), width=20, command=顯示參數結果).pack(pady=5)
    tk.Button(主視窗, text="關閉程式", font=("Arial", 12), width=20, command=主視窗.destroy).pack(pady=20)

    主視窗.mainloop()

if __name__ == "__main__":
    建立主選單()
