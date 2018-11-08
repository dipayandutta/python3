from tkinter import *
import sqlite3


class LoginApplication(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Login Application")
        self.pack(fill=BOTH, expand=1)
        self.centreWindow()

    def centreWindow(self):

        width =
