
import tkinter as tk

#from zmq import Frame  # 載入 tkinter 模組
from 模塊.視窗至中模塊 import 視窗至中  # 載入視窗至中模組
import 模塊.語言設定模塊 as 語言模型設定模塊  # 載入語言模型設定模塊
import 模塊.讀檔模塊 as 讀檔模塊  # 載入讀檔模塊
import 模塊.儲存設定檔 as 模型設定模塊  # 載入儲存模型設定檔模塊


def 模型設定視窗口():
    模型設定視窗的標題 = 語言模型設定模塊.語言['模型設定視窗標題']
    模型設定的取消按鈕 = 語言模型設定模塊.語言['模型設定的取消按鈕']
    模型設定的儲存並關閉按鈕 = 語言模型設定模塊.語言['模型設定的儲存並離開按鈕']

    # 創建主視窗
    模型設定視窗 = tk.Tk()
    模型設定視窗.title(模型設定視窗的標題)
    模型設定視窗.resizable(False,False)
    視窗至中(模型設定視窗)

    ### 讀取模型設定值 ###
    當前模型設定 = 模型設定模塊.讀取模型設定()  # 這裡會回傳 {"語言": ..., "顏色": ...}
    當前ollama開關 = 當前模型設定.get("ollama開關", "false")
    當前ollama模型 = 當前模型設定.get("ollama模型", "Ｎ＃Ａ")

    def 更新模型設定並關閉():
        模型設定模塊.寫入模型設定(
        )
        模型設定視窗.destroy()









    取消和儲存並關閉按鈕=tk.Frame(模型設定視窗)
    取消和儲存並關閉按鈕.place(relx=0.98,rely=0.98,anchor="se")
    # 按鈕
    取消按鈕 = tk.Button(取消和儲存並關閉按鈕, text=模型設定的取消按鈕, command=模型設定視窗.destroy)
    取消按鈕.grid(column=0, row=0, sticky="ew", padx=8, pady=0.1)
    
    儲存並關閉按鈕 = tk.Button(取消和儲存並關閉按鈕, text=模型設定的儲存並關閉按鈕, command=更新模型設定並關閉)
    儲存並關閉按鈕.grid(column=1, row=0, sticky="ew", padx=0.1, pady=0.1)

    模型設定視窗.mainloop()

if __name__ == "__main__":
    模型設定視窗口()