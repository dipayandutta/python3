from tkinter import Tk, BOTH,RIGHT , RAISED
from tkinter.ttk import Frame , Button , Style

class Example(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Button Application")
        self.style = Style()
        self.style.theme_use("default")
        self.pack(fill=BOTH,expand=1)
        self.centreWindow()
        self.frame()
        self.buttons()

    def centreWindow(self):

        width = 200
        height = 180

        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()

        x = (sw-width)/2
        y = (sh-height)/2

        self.master.geometry('%dx%d+%d+%d'%(width,height,x,y))


    def frame(self):
        frame = Frame(self,relief=RAISED,borderwidth=1)
        frame.pack(fill=BOTH,expand=True)


    def buttons(self):
        closeButton = Button(self,text="close",command=self.closePress)
        closeButton.pack(side=RIGHT,padx=5,pady=5)
        okButton = Button(self,text="OK",command=self.okPress)
        okButton.pack(side=RIGHT)

    def closePress(self):
        print ("Clicked on Close Button!")

    def okPress(self):
        print ("Clicked on OK Button!")


def main():
    root = Tk()
    root.geometry("300x200+300+300")
    application = Example()
    root.mainloop()

if __name__ == '__main__':
    main()

        


        
