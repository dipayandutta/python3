from tkinter import *

def main():
    myroot = Tk()
    myroot.title("Highlight Background")
    myroot.resizable(width=True,height=True)
    myEntry1 = Entry(myroot,bg='LightGreen',highlightthickness=10,highlightbackground="red",highlightcolor='Yellow')
    myEntry1.pack(padx=5,pady=5)

    myEntry2 = Entry(myroot)
    myEntry2.pack()
    myEntry2.focus()

    # Button Add
    buttonOK = Button(myroot,text='OK',command=printData)
    buttonOK.pack()

    myroot.mainloop()


def printData():
    print("Hello World!")

if __name__ == '__main__':
    main()