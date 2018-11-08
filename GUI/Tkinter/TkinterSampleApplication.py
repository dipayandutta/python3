from tkinter import *
from tkinter.ttk import *
import sys


class SampleApplication(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()
        self.centreWindow()
        self.swdesign()
        self.quitButton()

    def initUI(self):
        self.master.title('Sample Application')
        self.pack()

    def centreWindow(self):

        width = 400
        height = 250

        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()

        x = (sw-width)/2
        y = (sh-height)/2

        self.master.geometry('%dx%d+%d+%d' % (width, height, x, y))

    def swdesign(self):

        #-----------------------LAST NAME LABEL---------------#
        self.lastName_label = Label(self, text="Last Name".upper(), width=20)
        self.lastName_label.grid(row=0, column=0, sticky=W, padx=5, pady=10)
        #-----------------------LAST NAME ENTRY----------------#
        self.lastName_Entry = Entry(self, width=40)
        self.lastName_Entry.grid(row=0, column=1, sticky=W, padx=5, pady=10)
        #-----------------------FIRST NAME LABEL---------------#
        self.firstName_label = Label(self, text="First Name".upper(), width=20)
        self.firstName_label.grid(row=1, column=0, sticky=W, padx=5, pady=10)
        #-----------------------FIRST NAME ENTRY----------------#
        self.firstName_Entry = Entry(self, width=40)
        self.firstName_Entry.grid(row=1, column=1, sticky=W, padx=5, pady=10)

        #-----------------------JOB LABEL------------------------#
        self.job_Label = Label(self, text="job".upper(), width=20)
        self.job_Label.grid(row=2, column=0, sticky=W, padx=5, pady=10)
        #----------------------JOB ENTRY---------------------------#
        self.job_Entry = Entry(self, width=40)
        self.job_Entry.grid(row=2, column=1, sticky=W, padx=5, pady=10)

        #-----------------------COUNTRY LABEL-------------------#
        self.country_Label = Label(self, text="Country".upper(), width=20)
        self.country_Label.grid(row=3, column=0, sticky=W, padx=5, pady=10)
        #------------------------COUNTRY ENTRY-------------------#
        self.country_Entry = Entry(self, width=40)
        self.country_Entry.grid(row=3, column=1, sticky=W, padx=5, pady=10)

        #-------------------------SUBMIT BUTTON---------------------#
        submitButton = Button(self, text="submit".upper(),
                              command=self.getValue)
        submitButton.grid(row=4, column=1, sticky=W, padx=150, pady=30)

    def getValue(self):
        firstName = self.firstName_Entry.get()
        lastName = self.lastName_Entry.get()
        job = self.job_Entry.get()
        country = self.country_Entry.get()

        print(firstName)
        print(lastName)
        print(job)
        print(country)

    def quitButton(self):
        self.style = Style()
        self.style.theme_use("default")

        quitButton = Button(self, text="Quit".upper(),
                            command=self.quitApplication)
        quitButton.grid(row=4, column=0, sticky=W, padx=20, pady=30)

    def quitApplication(self):
        print("Quiting from Application....")
        sys.exit(1)


def main():
    root = Tk()
    application = SampleApplication()
    # root.geometry("300x300+200+200")
    root.mainloop()


if __name__ == '__main__':
    main()
