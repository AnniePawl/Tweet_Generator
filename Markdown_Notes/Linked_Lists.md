# Linked Lists Notes
A linked list is a linear data structure where each element is a separate object
    - Link list objects are not stored in contiguous order
    - A collection nodes, which together represent a sequence
    - Different storage space at each index
    - Dynamic, new piece of memory allocated to grow
    - Each node contains data and a reference (a link)
    - Each element points to the next
    - Entry point is called "head"
    - Last node is called "tail"
    - Can contain almost all datatypes
    - Can have unique and duplicate elements

### Benefits
- Can contain pretty much all data types
- Structure allows efficient insertion and removal of elements from any position in the sequence
- Dynamic size
- Overflow can't happen unless memory is actually full
- Moving pointers in easy

### Drawbacks
- Access time is linear, sequential from first node
- No random access
- Pointers take up space
- Not cache friendly

### Types of Linked Lists
**Singly Linked List:** Described above. Operations that can be performed on a single linked list include *insertion, deletion and traversal* </br>
**Doubly Linked List:** Has two references, one to next node and one to previous node.

### Runtime
- Access element via index O(n)
- Insert or delete element at beginning O(n)
- Insert or delete element in the middle O(n)
- Insert or delete element at the end O(n)

### The Process
a. Dynamically allocate space for a new node </br>
b. Check to make sure we didn't run out of memory </br>
c. Initialize node's va1 field </br>
d. Initialize node's next field </br>
e. Return pointer to newly created node </br>


### Grocery Store Example
`[ ("spinach") -> ("beans") -> ("rice") -> ("oil") ]`

In this notation, the [] denotes the linked list, each () represents a node, and each -> represents a reference, or link.

- The node with item "spinach" is the head of the linked list
- The node with item "beans" is the next node after the head
- The node with item "oil" is the tail of the linked list
- There are 4 nodes in this linked list

Nodes don't have indexed elements, so we don't have to shift anything around, just change reference on a single node. To add a node to the end of the list, just create a new node and add a reference to it from the last node, the tail of the list. To add a node to the beginning of the list, just create a new node and make a reference to the head.  
