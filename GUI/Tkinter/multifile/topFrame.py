from tkinter import *

class topFrame:
	def __init__(self,root,Top):
		self.root = root
		self.Top = Top

		lbl_title = Label(Top,text="Login Application",font=('arial',15))
		lbl_title.pack(fill=X)