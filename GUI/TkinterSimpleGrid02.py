from tkinter import *
from tkinter.ttk import *

class Example(Frame):

    def __init__(self):
        super().__init__()
        
        self.initUI()
        self.centreWindow()
        self.username_password()


    def initUI(self):

        self.master.title("Application")
        self.pack()
        
        
    def centreWindow(self):
        pass

    def username_password(self):

        #---------------------------USERNAME LABEL------------------#
        self.username_label = Label(self,text="username".upper(),width=20)
        self.username_label.grid(row=0,column=0,sticky=W,padx=10,pady=10)
        #----------------------------USERNAME ENTRY------------------#
        self.username_entry = Entry(self)
        self.username_entry.grid(row=0,column=1,padx=10,pady=10)
        #---------------------------PASSWORD LABEL--------------------#
        self.password_label = Label(self,text="password".upper(),width=20)
        self.password_label.grid(row=1,column=0,sticky=W,padx=10,pady=10)
        #---------------------------PASSWORD ENTRY---------------------#
        self.password_entry = Entry(self)
        self.password_entry.grid(row=1,column=1,padx=10,pady=10)
        #--------------------------LOGIN BUTTON--------------------------#
        loginButton = Button(self,text="login".upper(),command=self.click)
        loginButton.grid(row=2,column=1,padx=10,pady=10)

    def click(self):
        #---------------------------GETTING USERNAME AND PASSWORD VALUE-----------------------#
        username = self.username_entry.get()
        password = self.password_entry.get()

        print(username)
        print(password)
        
def main():
    root= Tk()
    root.geometry("300x300+200+200")
    application = Example()
    root.mainloop()


if __name__ == "__main__":
    main()
    
