from tkinter import Tk, Frame, Menu


class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.master.title("Submenu Application")

        #------------------------------CREATING MENUBAR----------------------#
        menuBar = Menu(self.master)
        self.master.config(menu=menuBar)
        #-----------------------------CREATING FILE MENU-----------------------#
        fileMenu = Menu(menuBar)
        #-----------------------------CREATING SUBMENU--------------------------#
        submenu = Menu(fileMenu)
        submenu.add_command(label="Hello", command=self.onClick)
        submenu.add_command(label="World")
        #------------------------------ADDING CASCADE---------------------------#
        fileMenu.add_cascade(label='Import', menu=submenu, underline=0)
        #------------------------------ADDING SEPARATOR--------------------------#
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", underline=0, command=self.onExit)

        menuBar.add_cascade(label="File", underline=0, menu=fileMenu)

        editMenu = Menu(menuBar)
        menuBar.add_cascade(label="Edit", underline=0)

    def onClick(self):
        print("Hello World!")

    def onExit(self):
        self.quit()


def main():
    root = Tk()
    root.geometry("300x300+250+200")
    application = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
