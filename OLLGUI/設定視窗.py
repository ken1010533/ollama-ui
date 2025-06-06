import tkinter as tk
import tkinter.ttk as ttk
from 模塊.視窗至中模塊 import 設定視窗至中
import 模塊.語言設定模塊 as 語言設定模塊
import 模塊.讀檔模塊 as 讀檔模塊
import 模塊.儲存設定檔 as 設定模塊
設定頁面視窗 = None  # 全域變數，儲存設定頁面視窗的實例
def 設定頁面視窗口():
    global 設定頁面視窗

    設定頁面視窗的標題 = 語言設定模塊.語言['設定視窗標題']
    設定的顏色切換 = 語言設定模塊.語言['顏色切換設定']['切換顏色']
    設定的顏色切換_白色 = 語言設定模塊.語言['顏色切換設定']['白色']
    設定的顏色切換_黑色 = 語言設定模塊.語言['顏色切換設定']['黑色']
    設定的語言翻譯 = 語言設定模塊.語言['語言選單']
    設定的取消按鈕 = 語言設定模塊.語言['設定的取消按鈕']
    設定的儲存並關閉按鈕 = 語言設定模塊.語言['設定的儲存並離開按鈕']

    # 建立子視窗（不是 Tk()，改為 Toplevel）
    if 設定頁面視窗 is None or not 設定頁面視窗.winfo_exists():
        設定頁面視窗 = tk.Toplevel()
        設定頁面視窗.title(設定頁面視窗的標題)
        設定頁面視窗.resizable(False, False)
        設定視窗至中(設定頁面視窗)

    # 讀取設定
    當前設定 = 設定模塊.讀取設定()
    當前語言 = 當前設定.get("語言", "")
    當前顏色 = 當前設定.get("顏色", "")

    # 顏色切換部分
    顏色切換的格式 = tk.Frame(設定頁面視窗)
    顏色切換的格式.grid()
    顏色設定標題 = tk.Label(顏色切換的格式, text=設定的顏色切換)
    顏色設定標題.grid(column=0, row=1)

    以切換到的顏色 = tk.StringVar(value=當前顏色 if 當前顏色 else 設定的顏色切換_白色)

    顏色_白色 = tk.Radiobutton(
        顏色切換的格式,
        text=設定的顏色切換_白色,
        variable=以切換到的顏色,
        value=設定的顏色切換_白色
    )
    顏色_黑色 = tk.Radiobutton(
        顏色切換的格式,
        text=設定的顏色切換_黑色,
        variable=以切換到的顏色,
        value=設定的顏色切換_黑色
    )

    顏色_白色.grid(column=1, row=1)
    顏色_黑色.grid(column=2, row=1)

    # 語言選單部分
    語言選單的格式 = tk.Frame(設定頁面視窗)
    語言選單的格式.grid_columnconfigure(1, weight=1)
    語言選單的格式.grid(padx=2.5, pady=2.5, sticky="ew")

    語言選單標題 = ttk.Label(語言選單的格式, text=設定的語言翻譯)
    語言選單標題.grid(column=0, row=1, sticky="ew")

    語言選單 = ttk.Combobox(
        語言選單的格式,
        values=讀檔模塊.語言翻譯,
        state="readonly"
    )
    語言選單.grid(column=1, row=1, sticky="ew", ipadx=20)
    語言選單.set(當前語言 if 當前語言 else 讀檔模塊.語言翻譯[0])

    # 儲存與取消按鈕
    按鈕區塊 = tk.Frame(設定頁面視窗)
    按鈕區塊.place(relx=0.98, rely=0.98, anchor="se")

    def 更新設定並關閉():
        設定模塊.寫入設定(
            語言=語言選單.get(),
            顏色=以切換到的顏色.get()
        )
        設定頁面視窗.destroy()

    取消按鈕 = tk.Button(按鈕區塊, text=設定的取消按鈕, command=設定頁面視窗.destroy)
    取消按鈕.grid(column=0, row=0, sticky="ew", padx=8, pady=0.1)

    儲存按鈕 = tk.Button(按鈕區塊, text=設定的儲存並關閉按鈕, command=更新設定並關閉)
    儲存按鈕.grid(column=1, row=0, sticky="ew", padx=0.1, pady=0.1)