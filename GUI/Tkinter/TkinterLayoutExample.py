from tkinter import *
from tkinter.ttk import Frame , Label , Entry

class Example(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):

        self.master.title("Layout Application")
        self.pack(fill=BOTH,expand=True)

        #-----------------Frame1--------------------#

        frame1 = Frame(self)
        frame1.pack(fill=X)

        lbl1 = Label(frame1,text="Title",width=6)
        lbl1.pack(side=LEFT,padx=5,pady=5)

        entry1 = Entry(frame1)
        entry1.pack(fill=X,padx=5,expand=True)

        #----------------Frame2-----------------------#

        frame2 = Frame(self)
        frame2.pack(fill=X)

        lbl2 = Label(frame2,text="Author",width=6)
        lbl2.pack(side=LEFT,padx=5,pady=5)

        entry2 = Entry(frame2)
        entry2.pack(fill=X,padx=5,expand=True)


        #-----------------Frame3-----------------------#

        frame3 = Frame(self)
        frame3.pack(fill=X)

        lbl3 = Label(frame3,text="Review",width=6)
        lbl3.pack(side=LEFT,anchor=N,padx=5,pady=5)
        
        txt = Text(frame3)
        txt.pack(fill=BOTH,pady=5,padx=5,expand=True)

        #------------------Frame4-----------------------#

        frame4 = Frame(self)
        frame4.pack(fill=X)

        closeButton = Button(self,text="Close")
        closeButton.pack(side=RIGHT,padx=5,pady=5)
        



def main():
    root =Tk()
    root.geometry("300x300+300+300")
    application = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
