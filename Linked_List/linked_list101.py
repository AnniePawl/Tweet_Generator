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

# Print Linked List
    def listprint(self):
        printval = self.headval
    # Check to see if there's more
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    # Inserting node at BEGINNING
    def AtBeginning(self,newdata):
        NewNode = Node(newdata)
        # Update new nodes next val to existing node
        NewNode.nextval = self.headval
        self.headval = NewNode

    # Inserting node at END
    def AtEnd(self,newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval=NewNode

    # Inserting node in the MIDDLE
    def InBetween(self,middle_node,newdata):
        NewNode = Node(newdata)
        if middle_node is None:
            print("The mentioned node is missing")
            return
        # Update new nodes next val to existing node
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode

    # DELETING a Node
    def RemoveNode(self, Removekey):
        HeadVal = self.head

        if (HeadVal is not None):
            if(HeadVal.data == Removekey):
                self.head = HeadVal.next
                HeadVal = None
                return

        while (HeadVal is not None):
            if HeadVal.data == Removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.next

        if (HeadVal == None):
            return

        prev.next = HeadVal.next

        HeadVal = None


# List Variable
list = SLinkedList()
# Assign first node
list.headval = Node("Mon")
# Assign other nodes
e2 = Node("Tue")
e3 = Node("Wed")

# LINK THE NODES!
# Link first Node to the next
list.headval.nextval = e2
# Link second Node to third node
e2.nextval = e3

# Add new node to BEGINNING
list.AtBeginning("Sun")
# Add new node to Middle
list.InBetween(list.headval.nextval,"Fri")
#  Add new node to END
list.AtEnd("Thurs")


# Example Interface
mylist = LinkedList()
mylist.append('a')
mylist.append('b')
mylist.append('c')

mylist.head.data  # => 'a'
mylist.tail.data  # => 'c'
mylist.find(lambda data: data > 'b')  # => 'c'
mylist.delete('a')
mylist.head.data  # => 'b'

# Print List!

list.listprint()
