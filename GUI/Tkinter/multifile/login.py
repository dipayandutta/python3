from tkinter import *
import sqlite3
from HomeWindow import *

class Login:

    def __init__(self,root,Form,event=None):

        self.root = root
        self.Form = Form

        self.lbl_text = Label(self.Form)
        self.lbl_text.grid(row=2,columnspan=2)

        
            
    def loginLogic(self,USERNAME,PASSWORD,username,password):

        global conn , cursor
        conn    = sqlite3.connect("login_database.db")
        cursor  = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, username TEXT , password TEXT)")
        cursor.execute("SELECT * FROM `member` WHERE `username` = 'admin' AND `password`='admin'")
        if cursor.fetchone() is None:
            cursor.execute("INSERT INTO `member` (username,password) VALUES('admin','admin')")

        conn.commit()

        if username == "" or password == "":
            self.lbl_text.config(text="Please enter username and password")
        else:
            print(username)
            print(password)
            cursor.execute("SELECT * FROM `member` WHERE `username` = ? AND `password`=?",(username,password))

            if cursor.fetchone() is not None:
                print("Login Successful")
                hWindow = homeWindow()
                USERNAME.set("")
                PASSWORD.set("")
                self.lbl_text.config(text="")
            else:
                self.lbl_text.config(text="")
                self.lbl_text.config(text="Invalid username or password",fg="red")
                USERNAME.set("")
                PASSWORD.set("")
                

        cursor.close()
        conn.close
            