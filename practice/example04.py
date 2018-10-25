class StringProg(object):
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input("Please add some text")

    def printString(self):
        print(self.string)


strObject = StringProg()
strObject.getString()
strObject.printString()
