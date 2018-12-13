class Node:
    def __init__(self,dataval=None):
        self.dataval = dataval
        self.nextval = None


class SLinkedList:
    def __init__(self):
        self.headval = None

    def listPrint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval


list1 = SLinkedList()
list1.headval = Node("One")
item2 = Node("Two")
item3 = Node("Three")

list1.headval.nextval = item2
item2.nextval = item3

list1.listPrint()
