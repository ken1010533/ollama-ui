import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import subprocess
import threading
import time
import os
import signal


# 运行命令的函数
def run_command():
    def task():
        command = entry.get()  # 获取输入框的命令
        if not command.strip():
            messagebox.showwarning("警告", "请输入命令！")
            return

        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        for line in process.stdout:
            output_text.insert(tk.END, line)  # 插入文本框
            output_text.see(tk.END)  # 滚动到底部

        for line in process.stderr:
            output_text.insert(tk.END, line)
            output_text.see(tk.END)

    thread = threading.Thread(target=task)  # 新线程执行命令
    thread.start()


# 停止命令执行
def stop_command():
    global process
    if process:
        if os.name == "nt":  # Windows
            subprocess.call(["taskkill", "/F", "/PID", str(process.pid)], shell=True)
        else:  # Linux / Mac
            os.kill(process.pid, signal.SIGTERM)
        process = None
        output_text.insert(tk.END, "进程已停止\n")


# 获取复选框的状态
def get_checkbutton_status():
    status = check_var.get()
    messagebox.showinfo("复选框状态", f"复选框状态：{'选中' if status else '未选中'}")


# 获取单选按钮的选择
def get_radiobutton_status():
    status = radio_var.get()
    messagebox.showinfo("单选按钮状态", f"选中的选项是：{status}")


# 获取下拉菜单的选择
def get_option_status():
    status = option_var.get()
    messagebox.showinfo("下拉菜单状态", f"选择的选项是：{status}")


# 滚动进度条
def update_progress():
    for i in range(101):
        time.sleep(0.05)
        progress_bar['value'] = i
        root.update_idletasks()


# 创建主窗口
root = tk.Tk()
root.title("功能丰富的 GUI 应用")
root.geometry("600x500")

# 标签和输入框
label = tk.Label(root, text="请输入命令：")
label.pack()

entry = tk.Entry(root, width=50)
entry.pack()

# 运行按钮
run_button = tk.Button(root, text="运行命令", command=run_command)
run_button.pack()

# 停止按钮
stop_button = tk.Button(root, text="停止命令", command=stop_command)
stop_button.pack()

# 复选框
check_var = tk.IntVar()
checkbutton = tk.Checkbutton(root, text="同意条款", variable=check_var)
checkbutton.pack()

check_button = tk.Button(root, text="获取复选框状态", command=get_checkbutton_status)
check_button.pack()

# 单选按钮
radio_var = tk.StringVar(value="A")
radiobutton1 = tk.Radiobutton(root, text="选项 A", variable=radio_var, value="A")
radiobutton2 = tk.Radiobutton(root, text="选项 B", variable=radio_var, value="B")
radiobutton1.pack()
radiobutton2.pack()

radio_button = tk.Button(root, text="获取单选按钮状态", command=get_radiobutton_status)
radio_button.pack()

# 下拉菜单
option_var = tk.StringVar()
option_var.set("苹果")
option_menu = tk.OptionMenu(root, option_var, "苹果", "香蕉", "橘子")
option_menu.pack()

option_button = tk.Button(root, text="获取下拉菜单状态", command=get_option_status)
option_button.pack()

# 文本框
output_text = scrolledtext.ScrolledText(root, width=60, height=10)
output_text.pack()

# 进度条
progress_bar = ttk.Progressbar(root, length=30000, mode="determinate", maximum=1000)
progress_bar.pack()

progress_button = tk.Button(root, text="开始进度条", command=update_progress)
progress_button.pack()

# 运行主循环
root.mainloop()
