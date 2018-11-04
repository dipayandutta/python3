from tkinter import *
from tkinter.ttk import *

class Example(Frame):

    def __init__(self):
        super().__init__()
        
        self.initUI()


    def initUI(self):

        self.master.title("Application")
        self.pack()
        
        self.username_label = Label(self,text="username",width=20)
        self.username_label.grid(row=0,column=0,sticky=W,padx=10,pady=10)

        self.username_entry = Entry(self)
        self.username_entry.grid(row=0,column=1,padx=10,pady=10)



def main():
    root= Tk()
    root.geometry("300x300+200+200")
    application = Example()
    root.mainloop()


if __name__ == "__main__":
    main()
    
