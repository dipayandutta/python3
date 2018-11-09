from tkinter import *
from serverList import *

class MenuApplication:

	def __init__(self):

		self.root = Tk() 
		self.root.title("Home Page")

		width = 400
		height = 300

		screen_width = self.root.winfo_screenwidth()
		screen_height = self.root.winfo_screenheight()

		x = (screen_width/2) - (width/2)
		y = (screen_height/2) - (width/2)

		self.root.geometry("%dx%d+%d+%d"%(width,height,x,y))
		self.root.resizable(0,0)

		self.menubar()

	def menubar(self):
		menuBar = Menu(self.root)
		self.root.config(menu=menuBar)

		fileMenu = Menu(menuBar)
		fileMenu.add_command(label="Exit",command=self.onExit)
		fileMenu.add_command(label="Servers",command=self.serverlist)
		menuBar.add_cascade(label="File",menu=fileMenu)

	def onExit(self):
		self.root.destroy()

	def serverlist(self):
		slist = serverList()