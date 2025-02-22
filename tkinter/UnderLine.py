from tkinter import *

def main():
    myroot = Tk()
    myroot.resizable(width=True,height=True)
    myroot.title("UnderLine Example ")
    myLabel1 = Label(myroot,text='Python',width=20,height=2,underline=2,font=('calibri',15))
    myLabel1.pack()

    myroot.mainloop()

if __name__ == '__main__':
    main()