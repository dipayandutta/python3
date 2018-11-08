from tkinter import *
import sqlite3


class LoginAppliaction(Frame):

    def __init__(self):
        super().__init__()

        self.Top = Frame(self, bd=2, relief=RIDGE)
        self.Top.grid(padx=10)

        self.Form = Frame(self, height=200)
        self.Form.grid(pady=20)

        self.initUI()

    def initUI(self):
        self.master.title("Login Application")
        self.pack(fill=BOTH, expand=1)

        self.centreWindow()
        self.Database()
        # self.login()
        self.loginForm()

    def centreWindow(self):

        width = 200
        height = 180

        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()

        x = (sw-width)/2
        y = (sh-height)/2

        self.master.geometry('%dx%d+%d+%d' % (width, height, x, y))

    def Database(self):
        global conn, cursor
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS `MEMBER` (mem_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,username TEXT , password TEXT)")
        cursor.execute(
            "SELECT * FROM `MEMBER` WHERE `username`='admin' and `password`='admin'")

        if cursor.fetchone() is None:
            cursor.execute(
                "INSERT INTO `member` (username , password) VALUES ('admin','admin')")
            conn.commit()

    def loginForm(self):

        #---------------------------------Heading ------------------------------#
        lbl_title = Label(
            self.Top, text="Simple Login Application", font=('arial', 15))
        lbl_title.grid(row=0)

        #----------------------------------USERNAME LABEL-----------------------#
        lbl_username = Label(self.Form, text="username".upper(),
                             font=('arial', 14), bd=15)
        lbl_username.grid(row=1, column=0, sticky="e")

        #----------------------------------USERNAME ENTRY-------------------------#
        username = Entry(self, font=(14))
        username.grid(row=1, column=1)

        #--------------------------------PASSWORD LABEL---------------------------#
        lbl_password = Label(self, text="password".upper(), font=('aria', 15))
        lbl_password.grid(row=2, column=0, sticky="e")

        #-------------------------------PASSWORD ENTRY----------------------------#
        password = Entry(self, font=(14))
        password.grid(row=2, column=1, sticky='e')


def main():

    root = Tk()
    application = LoginAppliaction()
    root.mainloop()


if __name__ == '__main__':
    main()
