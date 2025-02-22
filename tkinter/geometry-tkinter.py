from tkinter import *

def main():
    myroot = Tk()
    myroot.geometry('300x150')
    myroot.title("Tkinter Geometry")
    mybtn = Button(myroot,text='Hello')
    mybtn.pack(side=TOP,padx = 5 , pady = 5)

    myroot.mainloop()

if __name__ == '__main__':
    main()
