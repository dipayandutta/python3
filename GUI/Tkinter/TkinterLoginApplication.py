from tkinter import *
import sqlite3


class LoginAppliaction(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title()
