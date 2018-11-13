import datetime
import time
from tkinter import *
from tkinter import messagebox

root = Tk()

root.title("MultiFrame Application")
root.geometry('1350x650+150+150') # 150+150 is the co-ordinate

#------------------------------------FRAMES---------------------------------#
#Frame use for banner 
Tops = Frame(root,width=1350,height=50,bd=8,relief="raise")
Tops.pack(side=TOP)

#Left Frame 
leftFrame = Frame(root,width=600,height=600,bd=8,relief="raise")
leftFrame.pack(side=LEFT)

# Right Frame
rightFrame = Frame(root,width=300,height=700,bd=8,relief="raise")
rightFrame.pack(side=RIGHT)

# Frame attached to the left Frame upper half
f1a = Frame(leftFrame,width=600,height=200,bd=20,relief="raise")
f1a.pack(side=TOP)
#Frame attached to the left Frame bottom half
f1b = Frame(leftFrame,width=600,height=600,bd=20,relief="raise")
f1b.pack(side=TOP)

# banner label
informationLabel = Label(Tops,font=('arial',60,'bold'),text= "MultiFrame Application ",bd=10)
informationLabel.grid(row=0,column=0)
#------------------------------------------FUNCTIONS-------------------------------#
def weeklyWages():
    pass

def applicationQuit():
    qExit = messagebox.askyesno("MultiFrame Application","Quit Application?")

    if qExit > 0:
       root.destroy()
       return 0

def applicationReset():
    Name.set("")
    Address.set("")
    Employer.set("")
    NINumber.set("")
    HoursWorked.set("")
    HoursWorked.set("")
    HourlyRate.set("")
    Tax.set("")
    OverTime.set("")
    GrossPay.set("")
    NetPay.set("")
    DateOfOrder.set("")
    txtPaySlip.delete("1.0",END)

def enterInformation():
    
#--------------------------------------VARIABLES-----------------------------------#
Name = StringVar()
Address = StringVar()
Employer = StringVar()
NINumber = StringVar()
HoursWorked = StringVar()
HourlyRate = StringVar()
Tax = StringVar()
OverTime = StringVar()
GrossPay = StringVar()
NetPay = StringVar()
DateOfOrder = StringVar()

#----------------------------------------------------------------------------------#
DateOfOrder.set(time.strftime("%d/%m/%Y"))
#---------------------------------------LABELS-------------------------------------#
# Name Label
lblName =Label(f1a,text="Name",font=('arial',14,'bold'),bd=20)
lblName.grid(row=0,column=0)
#Address Label
lblAddress = Label(f1a,text="Address",font=('aria',14,'bold'),bd=20)
lblAddress.grid(row=0,column=2)

#Employeer Label
lblEmployer = Label(f1a,text="Employer",font=('arial',16,'bold'),bd=20)
lblEmployer.grid(row=1,column=0)

#NInumber label
lblNINumber = Label(f1a,text="NI Number",font=('aria',16,'bold'),bd=20)
lblNINumber.grid(row=1,column=2)

#Working Hours label
lblHoursWorked = Label(f1a,text="Hours Worked",font=('arial',16,'bold'),bd=20)
lblHoursWorked.grid(row=2,column=0)

#Hourly rate label
lblHourlyRate = Label(f1a,text="Hourly Rate",font=('arial',16,'bold'),bd=20)
lblHourlyRate.grid(row=2,column=2)

#Tax label
lblTax = Label(f1a,text="Tax",font=('arial',16,'bold'),bd=20)
lblTax.grid(row=3,column=0)

#Overtime label
lblOverTime = Label(f1a,text="OverTime",font=('arial',16,'bold'),bd=20)
lblOverTime.grid(row=3,column=2)

#Gross Pay Label
lblGrossPay = Label(f1a,text="Gross Pay",font=('arial',16,'bold'),bd=20)
lblGrossPay.grid(row=4,column=0)

#Netpay Label
lblNetPay = Label(f1a,text="Net Pay",font=('arial',16,'bold'),bd=20)
lblNetPay.grid(row=4,column=2)

#-----------------------------------------ENTRY WIDGETS-----------------------------#
entryName = Entry(f1a,textvariable=Name,font=('arial',16,'bold'),bd=16,width=22,justify='left')
entryName.grid(row=0,column=1)

entryAddress = Entry(f1a,textvariable=Address,font=('arial',16,'bold'),bd=16,width=22,justify='left')
entryAddress.grid(row=0,column=3)

entryEmployer = Entry(f1a,textvariable=Employer,font=('arial',16,'bold'),bd=16,width=22,justify='left')
entryEmployer.grid(row=1,column=1)

entryNINumber = Entry(f1a,textvariable=NINumber,font=('arial',16,'bold'),bd=16,width=22,justify='left')
entryNINumber.grid(row=1,column=3)

entryHoursWorked = Entry(f1a,textvariable=HoursWorked,font=('arial',16,'bold'),bd=16,width=22,justify='left')
entryHoursWorked.grid(row=2,column=1)

entryHourlyRate = Entry(f1a,textvariable=HourlyRate,font=('arial',16,'bold'),bd=16,width=22,justify='left')
entryHourlyRate.grid(row=2,column=3)

entryTax = Entry(f1a,textvariable=Tax,font=('arial',16,'bold'),bd=16,width=22,justify='left')
entryTax.grid(row=3,column=1)

entryOverTime = Entry(f1a,textvariable=OverTime,font=('arial',16,'bold'),bd=16,width=22,justify='left')
entryOverTime.grid(row=3,column=3)

entryGrossPay = Entry(f1a,textvariable=GrossPay,font=('arial',16,'bold'),bd=16,width=22,justify='left')
entryGrossPay.grid(row=4,column=1)

entryNetPay = Entry(f1a,textvariable=NetPay,font=('arial',16,'bold'),bd=16,width=22,justify='left')
entryNetPay.grid(row=4,column=3)

#-------------------------------------------TEXT WIDGET-----------------------------#
lblPaySlip = Label(rightFrame,font=('arial',20,'bold'),textvariable=DateOfOrder)
lblPaySlip.grid(row=0,column=0)
txtPaySlip = Text(rightFrame,height=22,width=34,bd=16,font=('arial',12,'bold'))
txtPaySlip.grid(row=1,column=0)
#--------------------------------------------BUTTONS AT BOTTON-----------------------#
btnSalary = Button(f1b,text="Weekly Salary",command=weeklyWages,padx=16,pady=16,bd=8,fg="black",font=('arial',16,'bold'),width=14,height=1)
btnSalary.grid(row=0,column=0)

btnReset = Button(f1b,text="Reset",padx=16,pady=16,bd=8,fg="yellow",font=('arial',16,'bold'),width=14,height=1,command=applicationReset)
btnReset.grid(row=0,column=1)

btnPaySlip = Button(f1b,text="View PaySlip",padx=16,pady=16,fg="green",font=('arial',16,'bold'),width=14,height=1,command=enterInformation)
btnPaySlip.grid(row=0,column=2)

btnExit = Button(f1b,text="Exit",padx=16,pady=16,fg="red",font=('arial',16,'bold'),width=14,height=1,command=applicationQuit)
btnExit.grid(row=0,column=3)
#-------------------------------------------MAINLOOP--------------------------------#
# main program calling for running the application
root.mainloop()
