from tkinter import *
from tkinter import font

def main():
    myroot = Tk()
    myroot.resizable(width=True,height=True)

    fontList = list(font.families())

    for loop in fontList:
        print(loop,end=',')

    myroot.mainloop()
if __name__ == '__main__':
    main()