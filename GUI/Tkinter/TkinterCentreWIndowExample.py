from tkinter import Tk, BOTH
from tkinter.ttk import Frame

class Example(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Centred Window Application")
        self.pack(fill=BOTH,expand=1)
        self.centeredWindow()

    def centeredWindow(self):

        width = 130
        height = 150

        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()

        x = (sw-width)/2
        y = (sh-height)/2

        self.master.geometry('%dx%d+%d+%d'%(width,height,x,y))

def main():
    root = Tk()
    ex = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
