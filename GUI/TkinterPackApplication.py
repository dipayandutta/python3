#pack() Example
from tkinter import *

root = Tk()
root.geometry("400x400+100+200")

#------------Full Horizontal Label-----#
# First Label

lbl1 = Label(root,text="Label1",bg="#E74C3C",fg ="white")
lbl1.pack(fill=X , padx=10 , )

# Second Label #

lbl2 = Label(root,text="Label2",bg="#2ECC71",fg="black")
lbl2.pack(fill=X,padx=10)

# Third Label #
lbl3 = Label(root,text="Label3",bg="#F1C40F",fg="white")
lbl3.pack(fill=X,padx=10)


# side option of Label #

lbl4 = Label(root,text="Label4",bg="#34495E",fg="white")
lbl4.pack(fill=X,padx=10,pady=10,side=LEFT)

# Fifth label #
lbl5 = Label(root,text="Label5",bg="#5DADE2",fg="white")
lbl5.pack(fill=X,padx=10,side=LEFT)

# mainloop of the application
mainloop()
