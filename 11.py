import tkinter as tk
from tkinter import messagebox
import requests
import subprocess
import os

class GPTApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GPT 對話工具")

        # 模型選擇
        self.model_label = tk.Label(root, text="選擇模型:")
        self.model_label.pack()

        self.model_var = tk.StringVar()
        self.model_combobox = tk.OptionMenu(root, self.model_var, "Model 1", "Model 2", "Model 3")
        self.model_combobox.pack()

        # 輸入框
        self.input_label = tk.Label(root, text="請輸入訊息:")
        self.input_label.pack()

        self.input_entry = tk.Entry(root, width=50)
        self.input_entry.pack()

        # 對話顯示區域
        self.chat_box = tk.Text(root, height=10, width=50)
        self.chat_box.pack()

        # 送出按鈕
        self.send_button = tk.Button(root, text="送出", command=self.send_message)
        self.send_button.pack()

        # 日誌顯示區域
        self.log_box = tk.Text(root, height=5, width=50)
        self.log_box.pack()

        # 檢查版本按鈕
        self.check_version_button = tk.Button(root, text="檢查版本", command=self.check_version)
        self.check_version_button.pack()

    def send_message(self):
        model = self.model_var.get()
        message = self.input_entry.get()

        if not message:
            messagebox.showwarning("警告", "請輸入訊息")
            return

        # 顯示在聊天框
        self.chat_box.insert(tk.END, f"你: {message}\n")
        self.chat_box.yview(tk.END)

        # 呼叫 Ollama API (假設 URL 為 http://localhost:5000)
        response = self.get_gpt_response(model, message)
        
        if response:
            self.chat_box.insert(tk.END, f"GPT: {response}\n")
            self.chat_box.yview(tk.END)
        else:
            self.chat_box.insert(tk.END, "GPT: 無回應\n")
            self.chat_box.yview(tk.END)

    def get_gpt_response(self, model, message):
        try:
            # 假設 Ollama API 會以 POST 請求接收消息
            url = f"http://localhost:11434/ask"
            payload = {"model": model, "message": message}
            response = requests.post(url, json=payload)

            if response.status_code == 200:
                return response.json().get("reply")
            else:
                self.log_box.insert(tk.END, "無法連接到 Ollama\n")
                return None
        except Exception as e:
            self.log_box.insert(tk.END, f"錯誤: {e}\n")
            return None

    def check_version(self):
        # 假設 Ollama 的版本資訊可以通過命令行查詢
        try:
            result = subprocess.run(["ollama", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if result.returncode == 0:
                version = result.stdout.decode("utf-8").strip()
                messagebox.showinfo("版本資訊", f"Ollama 版本: {version}")
            else:
                messagebox.showerror("錯誤", "無法檢查版本")
        except Exception as e:
            messagebox.showerror("錯誤", f"檢查版本時發生錯誤: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = GPTApp(root)
    root.mainloop()
