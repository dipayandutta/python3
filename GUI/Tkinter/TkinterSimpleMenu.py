from tkinter import Tk, Frame, Menu


class Example(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.master.title("Simpel Menu Application")

        menuBar = Menu(self.master)
        self.master.config(menu=menuBar)

        fileMenu = Menu(menuBar)
        fileMenu.add_command(label="Exit", command=self.onExit)
        menuBar.add_cascade(label="File", menu=fileMenu)

    def onExit(self):
        self.quit()


def main():
    root = Tk()
    root.geometry("300x300+300+200")
    application = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
