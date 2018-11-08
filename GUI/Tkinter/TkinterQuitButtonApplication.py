from tkinter import Tk,BOTH
from tkinter.ttk import Frame , Button , Style
import sys

class Example(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Quit Button Application")
        self.pack(fill=BOTH,expand=1)
        self.centreWindow()
        self.quitButton()


    def centreWindow(self):

        width = 200
        height = 180

        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()

        x = (sw-width)/2
        y = (sh-height)/2

        self.master.geometry('%dx%d+%d+%d'%(width,height,x,y))

    def quitButton(self):

        self.style = Style()
        self.style.theme_use("default")

        quitButton = Button(self,text="Quit",command = self.quit)
        quitButton.place(x=50,y=50)

    def quit(self):
        print("Quit Button Clicked!!!")
        sys.exit(1)


def main():
    root = Tk()
    root.geometry("250x150+300+300")
    application = Example()
    root.mainloop()

if __name__ == '__main__':
    main()
        
