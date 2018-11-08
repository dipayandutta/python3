from tkinter import Tk, BOTH, Listbox, StringVar, END
from tkinter.ttk import Frame, Label


class Example(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("ListBox Application")
        self.pack(fill=BOTH, expand=1)

        acts = ['Scarlet Johansson', 'Rachel', 'Jessica Alba', 'Van Disel']

        lb = Listbox(self)

        for actress in acts:
            lb.insert(END, actress)

        lb.bind("<<ListboxSelect>>", self.onSelect)

        lb.pack(pady=15)

        self.var = StringVar()
        self.label = Label(self, text=0, textvariable=self.var)
        self.label.pack()

    def onSelect(self, val):
        sender = val.widget
        idx = sender.curselection()
        value = sender.get(idx)

        self.var.set(value)


def main():

    root = Tk()
    ex = Example()
    root.geometry("300x300+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()
