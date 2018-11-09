from tkinter import *
import sqlite3

root = Tk()
root.title("Login Application")

width = 400
height = 280

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)

root.geometry("%dx%d+%d+%d" % (width, height, x, y))

root.resizable(0, 0)

#----------------------------------DATABASE CONNECTION----------------------#


def Database():

    global conn, cursor
    conn = sqlite3.connect("login_database.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `member`(mem_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,username TEXT ,password TEXT)")
    cursor.execute(
        "SELECT * FROM `member` WHERE `username`='admin' AND `password`='admin'")
    if cursor.fetchone() is None:
        cursor.execute(
            "INSERT INTO `member` (username,password) VALUES ('admin','admin')")
        conn.commit()
#----------------------------------LOGIN METHOD-----------------------------#


def Login(event=None):
    Database()

    if USERNAME.get() == "" or PASSWORD.get() == "":
        lbl_text.config(text="Please enter username and password")
    else:
        cursor.execute("SELECT * FROM `member` WHERE `username` = ? AND `password`= ?",
                       (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            HomeWindow()
            USERNAME.set("")
            PASSWORD.set("")
            lbl_text.config(text="")
        else:
            lbl_text.config(
                text="Invalid Username or Password".upper(), fg="red")
            USERNAME.set("")
            PASSWORD.set("")

    cursor.close()
    conn.close()

#----------------------------------HOME WINDOW-----------------------------#


def HomeWindow():
    global Home
    root.withdraw()
    Home = Toplevel()
    Home.title("Login")

    width = 600
    height = 500

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.resizable(0, 0)

    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    design()

def design():
    lbl_home = Label(Home, text="Successfully Logedin",
                     font=('times new roman', 20)).pack()
    btn_back = Button(Home, text='Back', command=Back).pack(pady=20, fill=X)

#----------------------------------Back function --------------------------#
def Back():
    Home.destroy()
    root.deiconify()
#-----------------------------------VARIABLES-------------------------------#
USERNAME = StringVar()
PASSWORD = StringVar()

#-----------------------------------FRAMES-----------------------------------#
Top = Frame(root, bd=2, relief=RIDGE)
Top.pack(side=TOP, fill=X)

Form = Frame(root, height=200)
Form.pack(side=TOP, pady=20)

#---------------------------------LABLES---------------------------------------#
#----------------------------------HEADING-------------------------------------#
lbl_title = Label(Top, text="Simple Login Application", font=('arial', 15))
lbl_title.pack(fill=X)
#----------------------------------USERNAME LABEL------------------------------#
lbl_username = Label(Form, text="username".upper(), font=('arial', 14), bd=15)
lbl_username.grid(row=0, sticky="e")
#---------------------------------PASSWORD LABEL-------------------------------#
lbl_password = Label(Form, text="password".upper(), font=('arial', 14), bd=15)
lbl_password.grid(row=1, sticky="e")
#--------------------------------TEXT LABEL------------------------------------#
lbl_text = Label(Form)
lbl_text.grid(row=2, columnspan=2)


#-------------------------------ENTRY-------------------------------------------#
#-------------------------------USERNAME ENTRY----------------------------------#
username = Entry(Form, textvariable=USERNAME, font=(14))
username.grid(row=0, column=1)
#-------------------------------PASSWORD ENTRY-----------------------------------#
password = Entry(Form, textvariable=PASSWORD, show="*", font=(14))
password.grid(row=1, column=1)

#-----------------------------------BUTTON---------------------------------------#
btn_lgn = Button(Form, text="Login", width=45, command=Login)
btn_lgn.grid(pady=25, row=3, columnspan=2)
btn_lgn.bind('<Return>', Login)
