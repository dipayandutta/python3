from tkinter import *

root = Tk()
root.geometry("400x400+100+200")

Label(text="Label1",bg="#2ECC71",fg="black",width=10).grid(row=0,column=0)
Label(text="Label2",bg="#2ECC71",fg="black",width=10).grid(row=0,column=1)

Label(text="Label3",bg="#2ECC71",fg="black",width=10).grid(row=1,column=0)
Label(text="Label4",bg="#2ECC71",fg="black",width=10).grid(row=1,column=1)

Label(text="Label5",bg="#2ECC71",fg="black",width=10).grid(row=2,column=0)
Label(text="Label6",bg="#2ECC71",fg="black",width=10).grid(row=2,column=1)

mainloop()
