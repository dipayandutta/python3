from tkinter import *

def main():

    myroot = Tk()
    myroot.resizable(width=True,height=True)
    myroot.title("Buttons with padx and pady example")

    mybtn_col = Button(myroot,text="It is column no 4")
    mybtn_col.grid(row=0,column=4)

    mybtn_colspan = Button(myroot,text="The columnspan is 4")
    mybtn_colspan.grid(row=1,columnspan=4)

    mybtn_paddingx = Button(myroot,text="padx of 5 from outise widget border")
    mybtn_paddingx.grid(row=2,padx=5)

    mybtn_paddingy = Button(myroot,text="pady of 5 from outside widget border")
    mybtn_paddingy.grid(row=3,pady=5)

    mybtn_ipaddingx = Button(myroot,text ="ipadx of 5 from inside widget border")
    mybtn_ipaddingx.grid(row=4,ipadx=5)

    mybtn_ipaddingy = Button(myroot,text="ipady of 15 from inside widget border")
    mybtn_ipaddingy.grid(row = 5 , ipady=15)

    mybtn_row = Button(myroot,text="It's row no 7")
    mybtn_row.grid(row=7)

    myroot.mainloop()


if __name__ == '__main__':
    main()
