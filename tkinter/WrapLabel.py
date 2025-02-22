from tkinter import *

def main():
    myroot = Tk()
    myroot.title("Label Wrap Example")
    myroot.resizable(width=False,height=True)

    myLabel1 = Label(myroot,text='Python3',wraplength=1)
    myLabel1.pack()

    myLabel2 = Label(myroot,text='Hello World!',wraplength=0)
    myLabel2.pack()

    myroot.mainloop()

if __name__ == '__main__':
    main()