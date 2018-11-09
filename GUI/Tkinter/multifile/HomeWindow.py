from tkinter import *
from menu import *

class homeWindow:

	def __init__(self):
		appMenu = MenuApplication()
		appMenu.menubar()
		'''
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
		'''
		#self.design()
'''
	def design(self):

		appMenu.menubar()

	


		#lbl_home = Label(Home,text="Successfully Login",font=('times new roman',20)).pack(pady=20)
		#btn_back = Button(Home,text='Back',command=self.Back).pack(pady=20,fill=X)

		#btn_print = Button(Home,text="CLick",command=self.onClick).pack(pady=20,fill=X)

	def Back(self):
		Home.destroy()
		self.root.deiconify()

	def onClick(self):
		print("Hello World!")
'''
	