from tkinter import *

def main():

    myroot = Tk()
    myroot.geometry('340x400')

    myroot.title('Get Boolean Variable')

    # String varibale
    userString = StringVar()
    
    # user Input
    userdataInput = Entry(myroot,font=('calibri',12),textvariable=userString)
    userdataInput.grid(row=1,column=0)
     # Grab User data 

    def showuserData():
        userdataInput = userString.get()
        print(userdataInput)
        userString.set('')

    # Button to get the userinput in the terminal
    okButton = Button(myroot,font=('Calibri',12),text='display',command=showuserData)
    okButton.grid(row=4,column=1)

    # Boolean Var Iput
    userBoolData = BooleanVar()
    userStrData  = StringVar()


    # function for boolean Variable

    def boolData():
        if userBoolData.get() == True:
            userStrData.set('It is Set to True')
        else:
            userStrData.set('It is Set to False')
    userdataCheckBox=Checkbutton(myroot,variable=userBoolData,font=('Calibri',12),text='Check',command=boolData)
    userdataCheckBox.grid(row=2,column=1)

    booldataShow = Entry(myroot,width=20,textvariable=userStrData)
    booldataShow.grid(row=3,column=1)

   

    myroot.mainloop()

if __name__ == '__main__':
    main()
