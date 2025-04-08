import tkinter as tk
from tkinter import ttk, messagebox, filedialog, colorchooser, simpledialog, scrolledtext
from PIL import Image, ImageTk
import os

class TkinterDemoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter 功能全面介紹")
        self.root.geometry("900x700")
        
        # 創建主框架
        self.create_main_frame()
        
        # 創建選單欄
        self.create_menubar()
        
        # 創建工具欄
        self.create_toolbar()
        
        # 創建狀態欄
        self.create_statusbar()
        
        # 創建筆記本(分頁控件)
        self.create_notebook()
        
        # 初始化變數
        self.init_variables()
        
    def create_main_frame(self):
        """創建主框架"""
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
    def create_menubar(self):
        """創建選單欄"""
        menubar = tk.Menu(self.root)
        
        # 檔案選單
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="開啟檔案", command=self.open_file)
        file_menu.add_command(label="儲存檔案", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="退出", command=self.root.quit)
        menubar.add_cascade(label="檔案", menu=file_menu)
        
        # 編輯選單
        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="複製", command=lambda: self.text_event("copy"))
        edit_menu.add_command(label="貼上", command=lambda: self.text_event("paste"))
        edit_menu.add_command(label="剪下", command=lambda: self.text_event("cut"))
        menubar.add_cascade(label="編輯", menu=edit_menu)
        
        # 查看選單
        view_menu = tk.Menu(menubar, tearoff=0)
        self.theme_var = tk.StringVar()
        view_menu.add_radiobutton(label="淺色主題", variable=self.theme_var, value="light", command=self.change_theme)
        view_menu.add_radiobutton(label="深色主題", variable=self.theme_var, value="dark", command=self.change_theme)
        view_menu.add_radiobutton(label="系統主題", variable=self.theme_var, value="system", command=self.change_theme)
        self.theme_var.set("system")
        menubar.add_cascade(label="查看", menu=view_menu)
        
        # 幫助選單
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="關於", command=self.show_about)
        menubar.add_cascade(label="幫助", menu=help_menu)
        
        self.root.config(menu=menubar)
    
    def create_toolbar(self):
        """創建工具欄"""
        toolbar = ttk.Frame(self.main_frame)
        toolbar.pack(fill=tk.X, padx=2, pady=2)
        
        # 工具欄按鈕
        ttk.Button(toolbar, text="打開", command=self.open_file).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="保存", command=self.save_file).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="剪下", command=lambda: self.text_event("cut")).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="複製", command=lambda: self.text_event("copy")).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="貼上", command=lambda: self.text_event("paste")).pack(side=tk.LEFT, padx=2)
        
        # 分隔線
        ttk.Separator(toolbar, orient=tk.VERTICAL).pack(side=tk.LEFT, padx=5, fill=tk.Y)
        
        # 組合框
        self.combo_var = tk.StringVar()
        self.combo = ttk.Combobox(toolbar, textvariable=self.combo_var, width=15)
        self.combo['values'] = ('選項1', '選項2', '選項3', '選項4')
        self.combo.pack(side=tk.LEFT, padx=2)
        self.combo.bind("<<ComboboxSelected>>", self.combo_selected)
        
    def create_statusbar(self):
        """創建狀態欄"""
        self.status_var = tk.StringVar()
        self.status_var.set("就緒")
        
        statusbar = ttk.Frame(self.main_frame)
        statusbar.pack(fill=tk.X, side=tk.BOTTOM, pady=2)
        
        ttk.Label(statusbar, textvariable=self.status_var).pack(side=tk.LEFT)
        ttk.Label(statusbar, text="Tkinter 示範").pack(side=tk.RIGHT)
    
    def create_notebook(self):
        """創建筆記本(分頁控件)"""
        self.notebook = ttk.Notebook(self.main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # 創建各個分頁
        self.create_basic_widgets_tab()
        self.create_text_widget_tab()
        self.create_canvas_tab()
        self.create_treeview_tab()
        self.create_dialogs_tab()
    
    def create_basic_widgets_tab(self):
        """基本元件分頁"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="基本元件")
        
        # 使用網格布局
        row = 0
        
        # 標籤
        ttk.Label(tab, text="這是標籤(Label):").grid(row=row, column=0, sticky=tk.W, padx=5, pady=5)
        row += 1
        
        # 按鈕
        ttk.Button(tab, text="普通按鈕", command=lambda: self.show_message("按鈕點擊")).grid(row=row, column=0, sticky=tk.W, padx=5, pady=5)
        row += 1
        
        # 輸入框
        ttk.Label(tab, text="輸入框(Entry):").grid(row=row, column=0, sticky=tk.W, padx=5, pady=5)
        self.entry = ttk.Entry(tab)
        self.entry.grid(row=row, column=1, sticky=tk.W, padx=5, pady=5)
        ttk.Button(tab, text="顯示輸入", command=self.show_entry_content).grid(row=row, column=2, padx=5, pady=5)
        row += 1
        
        # 多行文本
        ttk.Label(tab, text="多行文本(Text):").grid(row=row, column=0, sticky=tk.NW, padx=5, pady=5)
        self.text = tk.Text(tab, width=40, height=5)
        self.text.grid(row=row, column=1, columnspan=2, sticky=tk.W, padx=5, pady=5)
        row += 1
        
        # 單選按鈕
        ttk.Label(tab, text="單選按鈕(Radiobutton):").grid(row=row, column=0, sticky=tk.W, padx=5, pady=5)
        self.radio_var = tk.StringVar(value="1")
        ttk.Radiobutton(tab, text="選項1", variable=self.radio_var, value="1").grid(row=row, column=1, sticky=tk.W, padx=5, pady=5)
        ttk.Radiobutton(tab, text="選項2", variable=self.radio_var, value="2").grid(row=row, column=2, sticky=tk.W, padx=5, pady=5)
        row += 1
        
        # 複選框
        ttk.Label(tab, text="複選框(Checkbutton):").grid(row=row, column=0, sticky=tk.W, padx=5, pady=5)
        self.check_var1 = tk.BooleanVar()
        self.check_var2 = tk.BooleanVar()
        ttk.Checkbutton(tab, text="選項A", variable=self.check_var1).grid(row=row, column=1, sticky=tk.W, padx=5, pady=5)
        ttk.Checkbutton(tab, text="選項B", variable=self.check_var2).grid(row=row, column=2, sticky=tk.W, padx=5, pady=5)
        row += 1
        
        # 滑動條
        ttk.Label(tab, text="滑動條(Scale):").grid(row=row, column=0, sticky=tk.W, padx=5, pady=5)
        self.scale_var = tk.DoubleVar()
        ttk.Scale(tab, from_=0, to=100, variable=self.scale_var, 
                 command=lambda v: self.status_var.set(f"滑動條值: {float(v):.1f}")).grid(row=row, column=1, columnspan=2, sticky=tk.EW, padx=5, pady=5)
        row += 1
        
        # 進度條
        ttk.Label(tab, text="進度條(Progressbar):").grid(row=row, column=0, sticky=tk.W, padx=5, pady=5)
        self.progress = ttk.Progressbar(tab, orient=tk.HORIZONTAL, length=200, mode='determinate')
        self.progress.grid(row=row, column=1, columnspan=2, sticky=tk.W, padx=5, pady=5)
        ttk.Button(tab, text="開始", command=self.start_progress).grid(row=row+1, column=1, padx=5, pady=5)
        ttk.Button(tab, text="停止", command=self.stop_progress).grid(row=row+1, column=2, padx=5, pady=5)
        row += 2
        
        # 列表框
        ttk.Label(tab, text="列表框(Listbox):").grid(row=row, column=0, sticky=tk.NW, padx=5, pady=5)
        self.listbox = tk.Listbox(tab, height=4)
        self.listbox.grid(row=row, column=1, sticky=tk.W, padx=5, pady=5)
        for item in ["項目1", "項目2", "項目3", "項目4"]:
            self.listbox.insert(tk.END, item)
        ttk.Button(tab, text="顯示選擇", command=self.show_listbox_selection).grid(row=row, column=2, padx=5, pady=5)
        row += 1
        
        # 微調框
        ttk.Label(tab, text="微調框(Spinbox):").grid(row=row, column=0, sticky=tk.W, padx=5, pady=5)
        self.spinbox = ttk.Spinbox(tab, from_=0, to=10)
        self.spinbox.grid(row=row, column=1, sticky=tk.W, padx=5, pady=5)
        row += 1
    
    def create_text_widget_tab(self):
        """文本元件分頁"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="文本元件")
        
        # 滾動文本區域
        self.scrolled_text = scrolledtext.ScrolledText(tab, width=60, height=20, wrap=tk.WORD)
        self.scrolled_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # 插入示例文本
        sample_text = """Tkinter 是 Python 的標準 GUI 庫，它基於 Tk GUI 工具包。
        
這是 ScrolledText 元件示例，它自動帶有滾動條。

您可以在此輸入和編輯多行文本，並使用滾動條查看內容。

功能包括：
- 文本編輯
- 複製/貼上
- 查找/替換
- 文本格式化"""
        self.scrolled_text.insert(tk.END, sample_text)
    
    def create_canvas_tab(self):
        """畫布分頁"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="畫布")
        
        # 創建畫布
        self.canvas = tk.Canvas(tab, bg="white", width=600, height=400)
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # 繪製各種圖形
        self.canvas.create_rectangle(50, 50, 150, 150, fill="blue", outline="black")
        self.canvas.create_oval(200, 50, 300, 150, fill="red", outline="black")
        self.canvas.create_line(350, 50, 450, 150, width=3, fill="green")
        self.canvas.create_polygon(50, 200, 100, 300, 150, 200, fill="yellow", outline="black")
        self.canvas.create_arc(200, 200, 300, 300, start=0, extent=120, fill="orange")
        self.canvas.create_text(400, 250, text="這是畫布文字", font=('Arial', 12, 'bold'), fill="purple")
        
        # 添加圖片
        try:
            img = Image.open("python_logo.png" if os.path.exists("python_logo.png") else "python_logo.jpg")
            img = img.resize((100, 100), Image.Resampling.LANCZOS)
            self.tk_image = ImageTk.PhotoImage(img)
            self.canvas.create_image(500, 350, image=self.tk_image)
        except:  # noqa: E722
            self.canvas.create_text(500, 350, text="圖片未找到", fill="red")
    
    def create_treeview_tab(self):
        """樹形視圖分頁"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="樹形視圖")
        
        # 創建樹形視圖
        self.tree = ttk.Treeview(tab)
        self.tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # 添加數據
        root1 = self.tree.insert("", tk.END, text="根項目1", open=True)
        self.tree.insert(root1, tk.END, text="子項目1")
        self.tree.insert(root1, tk.END, text="子項目2")
        
        root2 = self.tree.insert("", tk.END, text="根項目2", open=True)
        self.tree.insert(root2, tk.END, text="子項目A")
        self.tree.insert(root2, tk.END, text="子項目B")
        
        # 表格視圖
        self.tree["columns"] = ("col1", "col2")
        self.tree.column("#0", width=150)
        self.tree.column("col1", width=100)
        self.tree.column("col2", width=100)
        
        self.tree.heading("#0", text="主欄位")
        self.tree.heading("col1", text="欄位1")
        self.tree.heading("col2", text="欄位2")
        
        item = self.tree.insert("", tk.END, text="數據項目", values=("值1", "值2"))
        self.tree.insert(item, tk.END, text="子數據", values=("A", "B"))
        
        # 添加按鈕框架
        btn_frame = ttk.Frame(tab)
        btn_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Button(btn_frame, text="新增項目", command=self.add_tree_item).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="刪除項目", command=self.remove_tree_item).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="顯示選擇", command=self.show_tree_selection).pack(side=tk.LEFT, padx=5)
    
    def create_dialogs_tab(self):
        """對話框分頁"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="對話框")
        
        # 對話框按鈕
        ttk.Button(tab, text="顯示訊息框", command=self.show_message_box).pack(fill=tk.X, padx=50, pady=10)
        ttk.Button(tab, text="顯示問題框", command=self.show_question_box).pack(fill=tk.X, padx=50, pady=10)
        ttk.Button(tab, text="顯示警告框", command=self.show_warning_box).pack(fill=tk.X, padx=50, pady=10)
        ttk.Button(tab, text="顯示錯誤框", command=self.show_error_box).pack(fill=tk.X, padx=50, pady=10)
        ttk.Button(tab, text="打開檔案對話框", command=self.open_file_dialog).pack(fill=tk.X, padx=50, pady=10)
        ttk.Button(tab, text="選擇顏色對話框", command=self.choose_color_dialog).pack(fill=tk.X, padx=50, pady=10)
        ttk.Button(tab, text="輸入對話框", command=self.show_input_dialog).pack(fill=tk.X, padx=50, pady=10)
    
    def init_variables(self):
        """初始化變數"""
        self.progress_value = 0
        self.progress_running = False
    
    # ========== 事件處理方法 ==========
    def show_message(self, message):
        """顯示訊息"""
        self.status_var.set(message)
    
    def show_entry_content(self):
        """顯示輸入框內容"""
        content = self.entry.get()
        self.show_message(f"輸入內容: {content}")
    
    def text_event(self, event):
        """文本操作事件"""
        if event == "copy":
            self.root.clipboard_clear()
            text = self.text.get("sel.first", "sel.last")
            self.root.clipboard_append(text)
        elif event == "paste":
            text = self.root.clipboard_get()
            self.text.insert("insert", text)
        elif event == "cut":
            self.root.clipboard_clear()
            text = self.text.get("sel.first", "sel.last")
            self.root.clipboard_append(text)
            self.text.delete("sel.first", "sel.last")
    
    def combo_selected(self, event):
        """組合框選擇事件"""
        selected = self.combo_var.get()
        self.show_message(f"選擇了: {selected}")
    
    def start_progress(self):
        """開始進度條"""
        if not self.progress_running:
            self.progress_running = True
            self.update_progress()
    
    def stop_progress(self):
        """停止進度條"""
        self.progress_running = False
    
    def update_progress(self):
        """更新進度條"""
        if self.progress_running:
            self.progress_value = (self.progress_value + 5) % 100
            self.progress['value'] = self.progress_value
            self.root.after(200, self.update_progress)
    
    def show_listbox_selection(self):
        """顯示列表框選擇"""
        selection = self.listbox.curselection()
        if selection:
            item = self.listbox.get(selection[0])
            self.show_message(f"選擇了: {item}")
        else:
            self.show_message("沒有選擇任何項目")
    
    def add_tree_item(self):
        """新增樹形視圖項目"""
        selected = self.tree.selection()
        if selected:
            parent = selected[0]
        else:
            parent = ""
        self.tree.insert(parent, tk.END, text="新項目", values=("新值1", "新值2"))
    
    def remove_tree_item(self):
        """刪除樹形視圖項目"""
        selected = self.tree.selection()
        if selected:
            self.tree.delete(selected[0])
    
    def show_tree_selection(self):
        """顯示樹形視圖選擇"""
        selected = self.tree.selection()
        if selected:
            item = self.tree.item(selected[0])
            text = item.get('text', '')
            values = item.get('values', [])
            self.show_message(f"選擇了: {text}, 值: {values}")
        else:
            self.show_message("沒有選擇任何項目")
    
    # ========== 對話框方法 ==========
    def show_message_box(self):
        """顯示訊息框"""
        messagebox.showinfo("訊息", "這是一個訊息對話框")
    
    def show_question_box(self):
        """顯示問題框"""
        result = messagebox.askquestion("問題", "這是一個問題對話框，是否繼續?")
        self.show_message(f"選擇結果: {'是' if result == 'yes' else '否'}")
    
    def show_warning_box(self):
        """顯示警告框"""
        messagebox.showwarning("警告", "這是一個警告對話框")
    
    def show_error_box(self):
        """顯示錯誤框"""
        messagebox.showerror("錯誤", "這是一個錯誤對話框")
    
    def open_file_dialog(self):
        """打開檔案對話框"""
        file_path = filedialog.askopenfilename(
            title="選擇檔案",
            filetypes=(("文本檔案", "*.txt"), ("所有檔案", "*.*"))
        )
        if file_path:
            self.show_message(f"選擇的檔案: {file_path}")
    
    def save_file(self):
        """儲存檔案對話框"""
        file_path = filedialog.asksaveasfilename(
            title="儲存檔案",
            defaultextension=".txt",
            filetypes=(("文本檔案", "*.txt"), ("所有檔案", "*.*"))
        )
        if file_path:
            self.show_message(f"檔案將儲存到: {file_path}")
    
    def open_file(self):
        """打開檔案"""
        self.open_file_dialog()
    
    def choose_color_dialog(self):
        """選擇顏色對話框"""
        color = colorchooser.askcolor(title="選擇顏色")
        if color[1]:
            self.show_message(f"選擇的顏色: {color[1]}")
    
    def show_input_dialog(self):
        """顯示輸入對話框"""
        result = simpledialog.askstring("輸入", "請輸入一些文字:")
        if result:
            self.show_message(f"輸入的文字: {result}")
    
    def show_about(self):
        """顯示關於對話框"""
        messagebox.showinfo("關於", "Tkinter 功能全面介紹\n版本 1.0\n© 2023")
    
    def change_theme(self):
        """更改主題"""
        theme = self.theme_var.get()
        if theme == "light":
            self.root.tk.call("set_theme", "light")
        elif theme == "dark":
            self.root.tk.call("set_theme", "dark")
        else:
            # 系統默認主題
            self.root.tk.call("set_theme", "default")

def main():
    root = tk.Tk()
    
    # 設置主題 (需要 ttkthemes 或系統支持)
    try:
        from ttkthemes import ThemedTk
        root = ThemedTk(theme="equilux")
    except:  # noqa: E722
        pass
    
    app = TkinterDemoApp(root)  # noqa: F841
    root.mainloop()

if __name__ == "__main__":
    main()