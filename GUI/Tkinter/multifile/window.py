from tkinter import *
from topFrame import *
from uiFrame import *

class MyLoginApplication:

    def __init__(self):
        self.root = Tk()
        self.root.title("Login Application")

        width = 400
        height = 280

        screen_width    = self.root.winfo_screenwidth()
        screen_height   = self.root.winfo_screenheight()

        x = (screen_width/2) - (width/2)
        y = (screen_height/2) -(height/2)

        self.root.geometry("%dx%d+%d+%d"%(width,height,x,y)) 
        self.root.resizable(0,0)

        self.Top = Frame(self.root,bd=2,relief=RIDGE)
        self.Top.pack(side=TOP,fill=X)

        self.Form = Frame(self.root,height=200)
        self.Form.pack(side=TOP,pady=20)

        

        self.TopPanel   = topFrame(self.root,self.Top)
        self.uiPanel    = uiFrame(self.root,self.Form)
        #self.loginPanel = Login(self.root,self.Form)



    def start(self):
        self.root.mainloop()