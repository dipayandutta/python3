class Node:
	 def __init__(self,dataval=None):
			self.dataval = dataval
			self.nextval = None

class LinkedList:
	 def __init__(self):
			self.headval = None


# Traverse the list
	 def listPrint(self):
			printval = self.headval
			while printval is not None:
				 print(printval.dataval)
				 printval = printval.nextval

# insert at the begining
	 def AtBeging(self,newData):
			newNode = Node(newData)
			newNode.nextval = self.headval
			self.headval  = newNode

item = LinkedList()
item.headval = Node("Zero")
item1 = Node("One")
item2 = Node("Two")

item.headval.nextval = item1
item1.nextval = item2

item.AtBeging("-1")

item.listPrint()
