from tkinter import *

def main():

    myroot = Tk()
    myroot.resizable(width=True,height=True)
    myroot.title("Buttons Example")

    myButton1 = Button(myroot,text='PYTHON',font=('Calibri',12),relief=FLAT,bd=4)
    myButton1.pack()

    myButton2 = Button(myroot,text='Python',font=('Calibri',11),relief=RAISED,bd=4)
    myButton2.pack()

    myButton3 = Button(myroot,text='PyThOn',font=('Calibri',12),relief='groove',bd=4)
    myButton3.pack()

    myButton4 = Button(myroot,text='Dipayan',font=('Calibri',12),relief='sunken',bd=12)
    myButton4.pack()

    myButton5 = Button(myroot,text='Hello',font=('Calibri',12),relief=RIDGE,bd=4)
    myButton5.pack()


    myroot.mainloop()

if __name__ == '__main__':
    main()

    
