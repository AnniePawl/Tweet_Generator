# IMPLEMENTING A LINKED LIST
class Node:
    # Constructor
    def __init__ (self, dataval=None):
        self.dataval = dataval
        self.nextval = None

# Singly Linked List
class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        # Check to see if there's more
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

# List Variable
list = SLinkedList()
# Assign first node
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
# Link first Node to the next
list.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3

list.listprint()
