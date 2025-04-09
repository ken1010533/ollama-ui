import tkinter as tk
from tkinter import ttk, simpledialog, messagebox, filedialog
import json

class 左側分頁應用程式:
    def __init__(self, root):
        self.root = root
        self.root.title("左側 Notebook（支援右鍵重新命名、儲存、載入）")
        self.root.geometry("800x500")

        self._建立樣式()
        self._建立介面()

    def _建立樣式(self):
        style = ttk.Style()
        style.theme_use("default")
        style.configure("左側樣式.TNotebook", tabposition="wn")
        style.layout("左側樣式.TNotebook.Tab", [
            ('Notebook.tab', {
                'sticky': 'nswe',
                'children': [
                    ('Notebook.padding', {
                        'side': 'top',
                        'children': [
                            ('Notebook.label', {'side': 'top', 'sticky': ''})
                        ]
                    })
                ]
            })
        ])

    def _建立介面(self):
        工具列 = tk.Frame(self.root)
        工具列.pack(side="top", fill="x")

        tk.Button(工具列, text="➕ 新增分頁", command=self.新增分頁).pack(side="left", padx=5, pady=5)
        tk.Button(工具列, text="💾 儲存", command=self.儲存分頁).pack(side="left", padx=5, pady=5)
        tk.Button(工具列, text="📂 載入", command=self.載入分頁).pack(side="left", padx=5, pady=5)

        self.筆記本 = ttk.Notebook(self.root, style="左側樣式.TNotebook",)
        self.筆記本.pack(expand=True, fill="both")

        # 右鍵選單
        self.右鍵選單 = tk.Menu(self.root, tearoff=0)
        self.右鍵選單.add_command(label="重新命名分頁", command=self.重新命名分頁)

        self.筆記本.bind("<Button-3>", self.處理右鍵點擊)

        self.分頁數 = 0
        self.新增分頁()

    def 處理右鍵點擊(self, event):
        點到分頁 = self.筆記本.index(f"@{event.x},{event.y}")
        self.目前右鍵分頁索引 = 點到分頁
        self.右鍵選單.post(event.x_root, event.y_root)

    def 重新命名分頁(self):
        原標題 = self.筆記本.tab(self.目前右鍵分頁索引, "text")
        新名稱 = simpledialog.askstring("重新命名分頁", f"請輸入新標題（原為：{原標題}）")
        if 新名稱:
            self.筆記本.tab(self.目前右鍵分頁索引, text=新名稱)

    def 新增分頁(self, 標題=None, 內容=None):
        self.分頁數 += 1
        框架 = tk.Frame(self.筆記本)
        文字框 = tk.Text(框架, wrap="word")
        文字框.pack(expand=True, fill="both", padx=10, pady=10)

        分頁標題 = 標題 if 標題 else f"分頁 {self.分頁數}"
        if 內容:
            文字框.insert("1.0", 內容)

        self.筆記本.add(框架, text=分頁標題)

    def 儲存分頁(self):
        所有資料 = []
        for i in range(self.筆記本.index("end")):
            框架 = self.筆記本.nametowidget(self.筆記本.tabs()[i])
            標題 = self.筆記本.tab(i, "text")
            內容 = 框架.winfo_children()[0].get("1.0", "end").strip()
            所有資料.append({"標題": 標題, "內容": 內容})

        路徑 = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON 檔案", "*.json")])
        if 路徑:
            with open(路徑, "w", encoding="utf-8") as f:
                json.dump(所有資料, f, ensure_ascii=False, indent=2)
            messagebox.showinfo("儲存完成", f"已儲存到：{路徑}")

    def 載入分頁(self):
        路徑 = filedialog.askopenfilename(filetypes=[("JSON 檔案", "*.json")])
        if 路徑:
            with open(路徑, "r", encoding="utf-8") as f:
                所有資料 = json.load(f)
            self._清除所有分頁()
            self.分頁數 = 0
            for 頁 in 所有資料:
                self.新增分頁(標題=頁["標題"], 內容=頁["內容"])
            messagebox.showinfo("載入成功", f"共載入 {len(所有資料)} 個分頁")

    def _清除所有分頁(self):
        for 分頁 in self.筆記本.tabs():
            self.筆記本.forget(分頁)

if __name__ == "__main__":
    root = tk.Tk()
    app = 左側分頁應用程式(root)
    root.mainloop()
