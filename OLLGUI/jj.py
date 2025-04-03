import tkinter as tk
from tkinter import ttk

# 原始選項數據
data_list = ["蘋果", "香蕉", "橘子", "葡萄", "梨子", "草莓", "芒果", "西瓜", "鳳梨", "櫻桃"]

def update_list(event):
    """在輸入時根據文本動態更新下拉選單，並保持下拉框開啟"""
    value = combobox.get()  # 獲取當前輸入的值
    filtered_values = [item for item in data_list if value in item]  # 過濾選項
    combobox['values'] = filtered_values  # 更新選單

    # 強制打開下拉選單
    combobox.tk.call("ttk::combobox::Post", combobox)

# 建立主視窗
root = tk.Tk()
root.title("Combobox 篩選（下拉選單保持顯示）")

# 建立 Combobox
combobox = ttk.Combobox(root, values=data_list)
combobox.pack(pady=10)
combobox.bind("<KeyRelease>", update_list)  # 綁定輸入事件

root.mainloop()