from tkinter import *

def main():
    myroot = Tk()

    myroot.geometry("340x340")
    myroot.resizable(width=True,height=True)
    myroot.title("Get User Input")

    # String Variable 
    mystr = StringVar()
    print(type(mystr))

    # Create an Entry for user input
    userdataEntry = Entry(myroot,font=('Calibri',12),textvariable=mystr)
    userdataEntry.pack()


    def showData():
        userDataEntry = mystr.get()
        print(userDataEntry)
        mystr.set('')

    okButton = Button(myroot,font=('Calibri',12),text='show',command=showData)
    okButton.pack()


    myroot.mainloop()

if __name__ == '__main__':
    main()
