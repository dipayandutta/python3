from tkinter import *

def main():

    myroot = Tk()
    myroot.title("Set Data in Entry")

    myroot.resizable(width=True,height=True)

    string = StringVar()
    myEntry1 = Entry(myroot,selectbackground='Green',selectforeground='Red',textvariable=string)
    myEntry1.pack()

    string.set('Python')

    myroot.mainloop()

if __name__ == '__main__':
    main()