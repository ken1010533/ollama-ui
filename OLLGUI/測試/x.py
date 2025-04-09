import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, filedialog
import json

主視窗 = tk.Tk()
主視窗.title("Notebook 終極強化版")
主視窗.geometry("1080x700")

# ---------- 主題樣式 ----------
style = ttk.Style()
style.theme_use("default")

# 主題樣式 = {
#     "light": {
#         "背景色": "#ffffff",
#         "文字色": "#000000",
#         "工具列色": "#dcdcdc",
#         "分頁色": "#e0e0e0"
#     },
#     "dark": {
#         "背景色": "#2e2e2e",
#         "文字色": "#ffffff",
#         "工具列色": "#444444",
#         "分頁色": "#3c3c3c"
#     }
# }
# 目前主題 = "light"

# ---------- 圖示 ----------
預設圖示 = tk.PhotoImage(width=1, height=1)  # 空白圖示預設用（可替換）

# ---------- 主結構 ----------
工具列框 = tk.Frame(主視窗, height=30)
工具列框.pack(side=tk.TOP, fill=tk.X)

分頁本 = ttk.Notebook(主視窗)
分頁本.pack(expand=1, fill="both")

# ---------- 分頁資料結構 ----------
分頁編號 = 0
分頁清單 = {}

# ---------- 功能 ----------

def 新增分頁(內容=""):
    global 分頁編號

    新頁面 = tk.Frame(分頁本)

    標籤 = tk.Label(新頁面, text="輸入內容：", font=("微軟正黑體", 12))
    標籤.pack(pady=10)

    輸入框 = tk.Entry(新頁面, width=40, font=("微軟正黑體", 12))
    輸入框.insert(0, 內容)
    輸入框.pack(pady=5)

    顯示區 = tk.Label(新頁面, text="", font=("微軟正黑體", 12), fg="blue")
    顯示區.pack(pady=10)

    def 顯示內容():
        顯示區.config(text=f"你輸入的是：{輸入框.get()}")

    確認鈕 = tk.Button(新頁面, text="確定", command=顯示內容, bg="#cccccc")
    確認鈕.pack()

    分頁名稱 = f"分頁 {分頁編號+1}"
    分頁本.add(新頁面, text=分頁名稱, image=預設圖示, compound="left")
    分頁清單[分頁名稱] = {"frame": 新頁面, "entry": 輸入框}
    分頁本.select(新頁面)
    分頁編號 += 1

def 關閉目前分頁():
    索引 = 分頁本.index("current")
    if 索引 >= 0:
        分頁名稱 = 分頁本.tab(索引, option="text")
        分頁本.forget(索引)
        分頁清單.pop(分頁名稱, None)

def 重新命名分頁():
    索引 = 分頁本.index("current")
    if 索引 >= 0:
        舊名稱 = 分頁本.tab(索引, option="text")
        新名稱 = simpledialog.askstring("重新命名", "請輸入新的分頁名稱：", initialvalue=舊名稱)
        if 新名稱:
            分頁本.tab(索引, text=新名稱)
            分頁清單[新名稱] = 分頁清單.pop(舊名稱)

def 儲存所有分頁():
    資料 = {名稱: 元件["entry"].get() for 名稱, 元件 in 分頁清單.items()}
    路徑 = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON 檔案", "*.json")])
    if 路徑:
        with open(路徑, "w", encoding="utf-8") as f:
            json.dump(資料, f, ensure_ascii=False, indent=2)
        messagebox.showinfo("成功", "資料已儲存！")

def 載入分頁資料():
    路徑 = filedialog.askopenfilename(filetypes=[("JSON 檔案", "*.json")])
    if 路徑:
        with open(路徑, "r", encoding="utf-8") as f:
            資料 = json.load(f)
        for 名稱, 內容 in 資料.items():
            新增分頁(內容)
            分頁本.tab("current", text=名稱)

def 分頁右鍵選單事件(event):
    try:
        索引 = 分頁本.index(f"@{event.x},{event.y}")
        分頁本.select(索引)
        分頁右鍵選單.tk_popup(event.x_root, event.y_root)
    finally:
        分頁右鍵選單.grab_release()

def 離開程式():
    主視窗.quit()

def 切換工具列顯示():
    if 工具列框.winfo_ismapped():
        工具列框.pack_forget()
    else:
        工具列框.pack(side=tk.TOP, fill=tk.X)

# ---------- 拖曳排序模擬 ----------
拖曳起始 = None
def 開始拖曳(event):
    global 拖曳起始
    拖曳起始 = 分頁本.index(f"@{event.x},{event.y}")

def 結束拖曳(event):
    global 拖曳起始
    if 拖曳起始 is None:
        return
    拖曳結束 = 分頁本.index(f"@{event.x},{event.y}")
    if 拖曳結束 != 拖曳起始:
        頁面 = 分頁本.tabs()[拖曳起始]
        分頁內容 = 分頁本.nametowidget(頁面)
        標題 = 分頁本.tab(拖曳起始, option="text")
        圖示 = 分頁本.tab(拖曳起始, option="image")

        分頁本.forget(拖曳起始)
        分頁本.insert(拖曳結束, 分頁內容)
        分頁本.tab(拖曳結束, text=標題, image=圖示, compound="left")
    拖曳起始 = None

分頁本.bind("<ButtonPress-1>", 開始拖曳)
分頁本.bind("<ButtonRelease-1>", 結束拖曳)

# ---------- 工具列 ----------
tk.Button(工具列框, text="➕ 新增分頁", command=新增分頁).pack(side=tk.LEFT, padx=5, pady=5)
tk.Button(工具列框, text="❌ 關閉分頁", command=關閉目前分頁).pack(side=tk.LEFT, padx=5, pady=5)
tk.Button(工具列框, text="✏️ 重新命名", command=重新命名分頁).pack(side=tk.LEFT, padx=5, pady=5)
tk.Button(工具列框, text="💾 儲存", command=儲存所有分頁).pack(side=tk.LEFT, padx=5, pady=5)
tk.Button(工具列框, text="📂 載入", command=載入分頁資料).pack(side=tk.LEFT, padx=5, pady=5)
# tk.Button(工具列框, text="🎨 主題切換", command=切換主題).pack(side=tk.LEFT, padx=5, pady=5)
tk.Button(工具列框, text="📏 收合工具列", command=切換工具列顯示).pack(side=tk.LEFT, padx=5, pady=5)
tk.Button(工具列框, text="🚪 離開", command=離開程式).pack(side=tk.RIGHT, padx=5, pady=5)

# ---------- 右鍵選單 ----------
分頁右鍵選單 = tk.Menu(主視窗, tearoff=0)
分頁右鍵選單.add_command(label="重新命名分頁", command=重新命名分頁)
分頁右鍵選單.add_command(label="關閉分頁", command=關閉目前分頁)
分頁本.bind("<Button-3>", 分頁右鍵選單事件)

# ---------- 啟動 ----------
新增分頁()
主視窗.mainloop()

