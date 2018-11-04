from tkinter import Tk, BOTH
from tkinter.ttk import Frame

class Example(Frame): #Application inhertes from the Frame class
    def __init__(self): # Constructor method
        super().__init__() #Constructor
        self.initUI() # main function for the application

    def initUI(self):

        self.master.title("Example") #set the title of the Application 
        self.pack(fill=BOTH,expand=1) #pack() one of the geometry method

def main():
    root = Tk() #This creates the window
    root.geometry("250x150+300+300") # Sets the geometry of the window
    app = Example() #creats the instance of the application 
    root.mainloop() # mainloop

if __name__ == '__main__':
    main()
