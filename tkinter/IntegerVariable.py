from tkinter import *

def main():
    
    myroot = Tk()
    myroot.geometry('400x320')
    myroot.title('Integer Calculation')
    myroot.resizable(0,0)

    myint = DoubleVar()
    myint1 = DoubleVar()
    myint2 = DoubleVar()

    myEntry = Entry(myroot,font=('Calibri',12),textvariable=myint)
    myEntry.pack()

    myEntry1 = Entry(myroot,font=('Calibri',12),textvariable=myint1)
    myEntry1.pack()



    def displayResult():
        mydata1 = myint.get()
        mydata2 = myint1.get()
        
        if (mydata1 > mydata2):
            result = mydata1 - mydata2
        else:
            result = mydata2 - mydata1

        myint2.set(result)

    resultButton = Button(myroot,font=('Calibri',12),text='Difference',command=displayResult)
    resultButton.pack()

    myEntry2 = Entry(myroot,font=('Calibri',12),textvariable=myint2)
    myEntry2.pack()
    myEntry2.configure(state='readonly')

    myroot.mainloop()

if __name__ == '__main__':
    main()
