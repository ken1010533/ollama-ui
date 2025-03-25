#宣告使用的函式庫
import tkinter as tk

# 创建窗口
root = tk.Tk()                             # 创建主窗口
root.title("功能丰富的 GUI 应用")           # 設定視窗標題
window_width = root.winfo_screenwidth()    # 取得螢幕寬度
window_height = root.winfo_screenheight()  # 取得螢幕高度
width = 600
height = 500
left = int((window_width - width)/2)       # 計算左上 x 座標
top = int((window_height - height)/2)      # 計算左上 y 座標
root.geometry(f'{width}x{height}+{left}+{top}')   # 設定視窗大小與位置
root.geometry("600x500")                   # 設定視窗大小
root.iconbitmap("1.ico")                   # 設定視窗圖示
root.resizable(True, True)                 # 設定視窗寬高可變動
# 設定背景圖片
# background_image = tk.PhotoImage(file="background.png")  # 載入背景圖片
# background_label = tk.Label(root, image=background_image,anchor=tk.N)  # 創建標籤以顯示圖片
# background_label.place(relwidth=1, relheight=1)  # 設定標籤大小與視窗相同

frame1=tk.Frame(root)
frame1.pack(side='bottom',fill="both")

# 标签和输入框
吉娃娃 = tk.Label(frame1,text="请输入：",font=("SimHei", 15),cursor="tcross")     #创建标签
吉娃娃.grid(column=2,row=2)                              #显示标签
entry = tk.Text(frame1, width=100,height=1)          #创建输入框
entry.grid(column=3,row=2)                             #显示输入框


root.mainloop()#窗口运行