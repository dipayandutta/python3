from tkinter import *
from login import *

class uiFrame:

	def __init__(self,root,From):
		self.root = root
		self.From = From 
		

		self.USERNAME = StringVar()
		self.PASSWORD = StringVar()

		lbl_username = Label(From,text="username".upper(),font=('arial',14),bd=15)
		lbl_username.grid(row=0,sticky="e")

		username = Entry(From,font=(14),textvariable=self.USERNAME)
		username.grid(row=0,column=1)

		lbl_password = Label(From,text="password".upper(),font=('arial',14),bd=15)
		lbl_password.grid(row=1,sticky="e")

		password = Entry(From,font=(14),show="*",textvariable=self.PASSWORD)
		password.grid(row=1,column=1)

		
		btn_lgn = Button(From,text="login",width=45,command=self.get)
		btn_lgn.grid(pady=25,row=3,columnspan=2)
		

	def get(self):
		user_name = self.USERNAME.get()
		pass_word = self.PASSWORD.get()
		

		lgn = Login(self.root,self.From)
		lgn.loginLogic(self.USERNAME,self.PASSWORD,user_name,pass_word)
		
		

