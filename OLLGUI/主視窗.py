import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import threading
from 模塊.視窗至中模塊 import 主視窗至中
import 模塊.語言設定模塊 as 語言設定模塊
import 模塊.檢查設備 as 檢查設備
import 設定視窗
import 模型視窗
import 模塊. ollama安裝檢查 as ollama安裝檢查
def 主視窗口():
    主視窗的標題 = 語言設定模塊.語言['主視窗']['主視窗標題']
    主視窗 = tk.Tk()
    主視窗.title(主視窗的標題)
    主視窗.resizable(False, False)
    主視窗至中(主視窗)

    if not ollama安裝檢查.檢查_ollama_是否安裝():
        messagebox.showerror("錯誤", "請檢查檔案完整性\"選項---->檢查\"")
        主視窗.destroy()


    主視窗的取消按鈕 = 語言設定模塊.語言['主視窗']['主視窗的關閉按鈕']
    主視窗的儲存並關閉按鈕 = 語言設定模塊.語言['主視窗']['主視窗的儲存並離開按鈕']
    開啟 = 語言設定模塊.語言['主視窗']['主視窗的檔案菜單的開啟']
    儲存 = 語言設定模塊.語言['主視窗']['主視窗的檔案菜單的儲存']
    關閉 = 語言設定模塊.語言['主視窗']['主視窗的檔案菜單的關閉']
    設定 = 語言設定模塊.語言['主視窗']['主視窗的設定按鈕']
    模型設定 = 語言設定模塊.語言['主視窗']['主視窗的模型設定按鈕']
    關於 = 語言設定模塊.語言['主視窗']['主視窗的其他菜單的關於']
    檢查更新 = 語言設定模塊.語言['主視窗']['主視窗的其他菜單的檢查更新']
    檔案 = 語言設定模塊.語言['主視窗']['主視窗的檔案菜單']
    選項 = 語言設定模塊.語言['主視窗']['主視窗的選項按鈕']
    其他 = 語言設定模塊.語言['主視窗']['主視窗的其他菜單']
    
    def 按鈕開啟():
        pass
    def 按鈕儲存():
        pass
    def 按鈕關閉():
        主視窗.destroy()
    def 按鈕設定():
        設定視窗.設定視窗口()
    def 按鈕模型設定():
        模型視窗.模型設定視窗口()
    def 按鈕關於():
        messagebox.showinfo("關於", "這是關於對話框的內容。")
    def 按鈕檢查更新():
       ollama安裝檢查.檢查_ollama_版本()
































    檢查設備結果 = 檢查設備.获取系统详情()
    if 檢查設備結果['是否为苹果设备']:
        主視窗的標題 += ' (Apple)'   # 建立選單
        主選菜單 = tk.Menu(主視窗)               # 建立主選單
        filemenu = tk.Menu(主選菜單)           # 建立子選單，選單綁定 主選菜單 主選單
        filemenu.add_command(label="Open")    # 子選單項目
        filemenu.add_command(label="Save")    # 子選單項目
        filemenu.add_command(label="Exit")    # 子選單項目
        主選菜單.add_cascade(label='File', menu=filemenu)   # 建立主選單，內容為子選單
        主視窗.config(menu=主選菜單)         # 將主選單綁定到主視窗 


    else:
        主視窗的標題 += ' (Windows)'
        menubar = tk.Menu(主視窗)



          









        # 檔案菜單
        檔案子菜單 = tk.Menu(menubar, tearoff=0)
        檔案子菜單.add_command(label=開啟,command=按鈕開啟)
        檔案子菜單.add_command(label=儲存, command=按鈕儲存)
        檔案子菜單.add_command(label=關閉, command=按鈕關閉)
        menubar.add_cascade(label=檔案, menu=檔案子菜單)

        # 選項菜單
        選項子菜單 = tk.Menu(menubar, tearoff=0)
        選項子菜單.add_command(label=設定, command=按鈕設定)
        選項子菜單.add_command(label=模型設定,command=按鈕模型設定)
        menubar.add_cascade(label=選項, menu=選項子菜單)

        # 其他菜單
        其他子菜單 = tk.Menu(menubar, tearoff=0)
        其他子菜單.add_command(label=關於, command=按鈕關於)
        其他子菜單.add_command(label=檢查更新,command=按鈕檢查更新)
        menubar.add_cascade(label=其他, menu=其他子菜單,command=按鈕檢查更新)
        主視窗.config(menu=menubar)




    # 建立 Notebook 樣式
    聊天視窗格式 = ttk.Style()
    聊天視窗格式.configure("TNotebook", tabposition='wn')

    聊天視窗 = ttk.Notebook(主視窗, style='TNotebook')
    聊天視窗.pack(expand=True, fill="both")

    # 🔽 關閉分頁函式（會取得當前選取的頁面）
    def 關閉目前分頁():
        所有分頁 = 聊天視窗.tabs()
        if len(所有分頁) <= 1:
            messagebox.showwarning("警告", "最後一個分頁不能關閉！")
            return

        當前分頁 = 聊天視窗.select()
        聊天視窗.forget(當前分頁)

    def 新增分頁(event=None):
        新頁面 = ttk.Frame(聊天視窗)
        聊天視窗.add(新頁面, text="新聊天")
        聊天視窗.select(新頁面)

        def 輸入(event=None):
            使用者輸入 = 輸入文本框.get()
            輸入文本框.delete(0, tk.END)

            if not 使用者輸入.strip():
                return

            輸出文本框.config(state=tk.NORMAL)
            輸出文本框.insert(tk.END, f"🧑‍💻 你：{使用者輸入}\n")
            回應標籤索引 = 輸出文本框.index(tk.END)
            輸出文本框.insert(tk.END, "🤖 回應：.\n")
            輸出文本框.config(state=tk.DISABLED)
            輸出文本框.see(tk.END)

            停止動畫 = threading.Event()

            def 動畫更新(點數=1):
                if 停止動畫.is_set():
                    return
                輸出文本框.config(state=tk.NORMAL)
                輸出文本框.delete(f"{float(回應標籤索引)-1} linestart", f"{float(回應標籤索引)}")
                輸出文本框.insert(tk.END, f"🤖 回應：{'.'*點數}\n")
                輸出文本框.config(state=tk.DISABLED)
                輸出文本框.see(tk.END)
                下一點數 = 1 if 點數 == 5 else 點數 + 1
                輸出文本框.after(500, lambda: 動畫更新(下一點數))

            輸出文本框.after(500, 動畫更新)

            def 處理回應():
                import time
                time.sleep(20)  # 模擬處理
                回應內容 = f"🤖 回應：你說的是「\n{使用者輸入}」嗎？"

                def 顯示回應():
                    停止動畫.set()
                    輸出文本框.config(state=tk.NORMAL)
                    輸出文本框.delete(f"{float(回應標籤索引)-1} linestart", f"{float(回應標籤索引)}")
                    輸出文本框.insert(tk.END, 回應內容 + "\n\n")
                    輸出文本框.config(state=tk.DISABLED)
                    輸出文本框.see(tk.END)

                輸出文本框.after(0, 顯示回應)

            threading.Thread(target=處理回應).start()

        輸出文本框 = tk.Text(新頁面, wrap="word", height=20, relief="ridge", borderwidth=1)
        輸出文本框.grid(column=3, row=2, sticky="nsew", padx=1, pady=1)
        輸出文本框.config(state=tk.DISABLED)

        滾動條輸出 = tk.Scrollbar(新頁面, command=輸出文本框.yview)
        輸出文本框.config(yscrollcommand=滾動條輸出.set)
        新頁面.grid_rowconfigure(2, weight=1)
        新頁面.grid_columnconfigure(3, weight=1)
        滾動條輸出.grid(column=4, row=2, sticky="ns")

        輸入文本框 = tk.Entry(新頁面, width=50)
        輸入文本框.grid(column=3, row=3, sticky="nsew", padx=1, pady=5)
        輸入文本框.bind("<Return>", 輸入)

        取消和儲存並關閉按鈕 = tk.Frame(新頁面)
        取消和儲存並關閉按鈕.grid(column=3, row=3, sticky=tk.E + tk.S, padx=1, pady=1)

        取消按鈕 = tk.Button(取消和儲存並關閉按鈕, text=主視窗的取消按鈕, command=關閉目前分頁)
        取消按鈕.grid(column=0, row=0, sticky=tk.W + tk.S, padx=8, pady=0.1)

        儲存並關閉按鈕 = tk.Button(取消和儲存並關閉按鈕, text=主視窗的儲存並關閉按鈕, command=新增分頁)
        儲存並關閉按鈕.grid(column=1, row=0, sticky=tk.W + tk.S, padx=0.1, pady=0.1)

        # 預設加入一頁
    新增分頁()














        # if 主視窗.
    def on_closing():
        if messagebox.askokcancel("關閉", "您確定要關閉視窗嗎?"):

            主視窗.destroy()
            模型視窗.模型設定視窗.destroy()
            設定視窗.設定視窗.destroy()

    主視窗.protocol("WM_DELETE_WINDOW", on_closing)
    主視窗.mainloop()

主視窗口()
