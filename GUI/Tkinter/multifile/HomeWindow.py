from tkinter import *

class homeWindow:

	def __init__(self,root):
		self.root = root
		global Home
		
		self.root.withdraw()
		Home=Toplevel()
		Home.title("Home Window")

		width = 600
		height = 500

		screen_width = self.root.winfo_screenwidth()
		screen_height = self.root.winfo_screenheight()

		x = (screen_width/2)-(width/2)
		y = (screen_height/2)-(height/2)

		self.root.resizable(0,0)

		Home.geometry("%dx%d+%d+%d"%(width,height,x,y))

		self.design()

	def design(self):
		lbl_home = Label(Home,text="Successfully Login",font=('times new roman',20)).pack()
		btn_back = Button(Home,text='Back',command=self.Back).pack(pady=20,fill=X)

	def Back(self):
		Home.destroy()
		self.root.deiconify()