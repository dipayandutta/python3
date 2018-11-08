from tkinter import *
from tkinter.ttk import *

root = Tk()
root.geometry("300x200+300+300")

def username_password(window):
    # username label #
    usename = Label(root,text="usename",width=20)
    usename.grid(row=0,column=0,sticky=W,padx=10,pady = 10)


    # usename entry #
    user_entry = Entry(root)
    user_entry.grid(row=0,column=1,padx= 10 , pady=10)

    # password label #
    password = Label(root , text="password",width =20)
    password.grid(row=1,column=0,sticky=W,padx=10 , pady=10)

    # password entry #
    pass_entry = Entry(root)
    pass_entry.grid(row=1,column=1, padx = 10  ,pady=10)

    # button grid #
    
    loginButton = Button(text="login",command=click)
    loginButton.grid(row=2,column=1,padx=10,pady=10)


def click():
    print (user_entry.get())

def main():
    username_password(root)



main()
