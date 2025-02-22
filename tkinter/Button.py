from tkinter import *

def main():
    myroot = Tk()
    myroot.resizable(width=False,height=False)
    myroot.title("Button Example")
    myButton1 = Button(myroot,text = 'Without highlight thickness')
    myButton1.grid(row=0,column=1)

    myButton2 = Button(myroot,text='With highlight thickness')
    myButton2.grid(row=1 , column=1 , padx=10 , pady=10)

    myButton3 = Button(myroot,activebackground="#ff0000",bg="#00ff00",text='Dipayan')
    myButton3.grid(row=2,column=1)

    myButton4 = Button(myroot,state='disabled',text='Kdump',disabledforeground='Magenta')
    myButton4.grid(row=3,column=1,padx=5,pady=5)
    
    myroot.mainloop()

if __name__ == '__main__':
    main()