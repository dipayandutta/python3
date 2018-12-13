class Node:
	 def __init__(self,dataVal):
			self.dataVal = dataVal
			self.nextVal = None

class LinkedList:
	 def __init__(self):
			self.headVal = None


	 # Function to add a new node at the BEGINING
	 def insertAtBeign(self,newData):
			NewNode = Node(newData)
			NewNode.nextVal = self.headVal
			self.headVal = NewNode

	 # Function to add a new node at the END
	 def insertAtEnd(self,newData):
			NewNode = Node(newData)
			if self.headVal is None:
				 self.headVal = NewNode
				 return

			last = self.headVal
			while(last.nextVal):
						last = last.nextVal
			last.nextVal = NewNode

	 # Print the linked List
	 def listPrint(self):
			printVal = self.headVal
			while printVal is not None:
				 print(printVal.dataVal)
				 printVal = printVal.nextVal


list_ = LinkedList()
list_.headVal = Node("One")
item1 = Node("Two")
item2 = Node("Three")

list_.headVal.nextVal = item1
item1.nextVal = item2

list_.insertAtEnd("Five")
list_.insertAtBeign("-2")
list_.listPrint()
