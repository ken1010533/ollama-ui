import tkinter as tk

# 預設的提示文字
default_text = "輸入任何問題"

def on_entry_focus_in(event):
    """當輸入框獲得焦點時，變更文字顏色"""
    entry.config(fg="black", insertbackground="black")  # 變成正常輸入顏色
    if entry.get() == default_text:
        entry.delete(0, tk.END)  # 清除內容

def on_entry_focus_out(event):
    """當輸入框失去焦點時，變更為淡淡的灰色文字"""
    if not entry.get():  # 如果輸入框是空的
        entry.insert(0, default_text)  # 插入提示文字
        entry.config(fg="gray", insertbackground="gray")  # 變淡

def on_key_release(event):
    """當使用者輸入時，變淡的文字顏色"""
    if entry.get() != default_text:
        entry.config(fg="gray")  # 讓輸入的文字顯示為灰色
    else:
        entry.config(fg="black")  # 如果是預設文字則顯示黑色

# 創建主視窗
root = tk.Tk()
root.title("對話框範例")
root.geometry("400x100")

# 創建輸入框
entry = tk.Entry(root, fg="gray", font=("Arial", 14))  
entry.insert(0, default_text)  # 插入提示文字
entry.bind("<FocusIn>", on_entry_focus_in)  # 當點擊輸入框時
entry.bind("<FocusOut>", on_entry_focus_out)  # 當離開輸入框時
entry.bind("<KeyRelease>", on_key_release)  # 當輸入文字時
entry.pack(pady=20, padx=20, fill="x")

# 啟動主迴圈
root.mainloop()
