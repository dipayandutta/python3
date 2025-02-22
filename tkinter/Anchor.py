from tkinter import *

def main():

    myroot = Tk()
    myroot.resizable(width=True,height=True)

    myroot.title("Anchor Example")
    myroot.geometry('200x200')

    myLabel1 = Label(myroot,text='Python',anchor=N ,font =("Calibri","18","bold italic underline"),bd=1,relief='sunken',width=10,height=5)

    myLabel1.pack()

    myroot.mainloop()

if __name__ == '__main__':
    main()