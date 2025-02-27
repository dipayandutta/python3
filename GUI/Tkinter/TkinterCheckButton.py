from tkinter import Tk, Frame, Checkbutton
from tkinter import BooleanVar, BOTH


class Example(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.master.title("CheckButton Application")
        self.pack(fill=BOTH, expand=True)
        self.var = BooleanVar()

        cb = Checkbutton(self, text="Show Title",
                         variable=self.var, command=self.onClick)
        cb.select()
        cb.place(x=50, y=50)

    def onClick(self):

        if self.var.get() == True:
            self.master.title("CheckButton Application")
        else:
            self.master.title("")


def main():

    root = Tk()
    root.geometry("300x200+300+300")
    application = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
