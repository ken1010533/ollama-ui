# 單一視窗.py
import tkinter as tk
from tkinter import Toplevel

class 單一視窗:
    def __init__(self, 主視窗, 標題="子視窗"):
        self.主視窗 = 主視窗
        self.視窗實體 = None
        self.標題 = 標題

    def 顯示(self, 建立內容函式=None):
        if self.視窗實體 is None or not self.視窗實體.winfo_exists():
            self.視窗實體 = Toplevel(self.主視窗)
            self.視窗實體.title(self.標題)
            self.視窗實體.protocol("WM_DELETE_WINDOW", self.關閉事件)

            if 建立內容函式:
                建立內容函式(self.視窗實體)
        else:
            self.視窗實體.lift()  # 已存在就移到最上層

    def 關閉事件(self):
        self.視窗實體.destroy()
        self.視窗實體 = None
