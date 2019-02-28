# GAME PLAN
    # Implement Length Method
    # Implement Append Method
    # Implement Prepend Method
    # Implement Find Method
    # Implement Delete Method
    # Implement Replace Method
    # Run and Pass all Unit Tests

class Node(object):

    def __init__(self, data):
        """Initialize this node with given data."""
        self.data = data
        self.next = None


    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)



class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node

        if items is not None: # Append items, if any
            for item in items:
                self.append(item)


    def __str__(self):
        """Return formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))


    def __repr__(self):
        """Return string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())


    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best case run time: O(n) for n items in list (length).
        Worst case run time: O(n), same """
        items = []  # O(1)to create empty list
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None (one node too far past tail)
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1)(on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable

        return items  # O(1) time to return list


    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None # O(1), just checking single value

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        Run time: O(n), iterates over all items to count"""
        counter = 0
        curr_node = self.head
        while curr_node is not None: # O(n), must iterate over every item (n nodes) to count each
            curr_node = curr_node.next
            counter += 1 # Increment size/ length

        return counter


    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Run time: O(1), we know tail and only change last node."""
        new_node = Node(item)

        if self.tail is not None: #Append node after tail
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node


    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Run time: O(1), we know head and only need to adjust first node"""
        new_node = Node(item)

        if self.head is not None: # Append node at beginning
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node


    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        Best case run time: O(1), if item is head or tail
        Worst case run time: O(n), if we must loop through each node"""
        curr_node = self.head
        # Loop thru all nodes, find where quality is true
        while curr_node is not None and not quality(curr_node.data):
            curr_node = curr_node.next
        if curr_node is None:
            return None

        return curr_node.data

    # This method still needs to be tested
    def replace(old_item, new_item):
        """ Replaces old item with new item without creating new node"""
        curr_node = self.head
        while curr_node is not None:
            if curr_node.data == old_item:
                current_node.data = new_item
                return
            else:
                raise ValueError('Item not found: {}'.format(item))


    def delete(self, item):
        """Delete the given item from linked list, or raise ValueError.
        Best case run time: O(1), linked list is empty or item is at head
        Worst case running time: O(n), might traverse entire linked list"""
        if self.head is None: # Raise error if list is empty
            raise ValueError('Item not found: {}'.format(item))

        if self.head.data == item: # Is item first node?
            self.head = self.head.next # If item at head, move head pointer around to next node
            if self.head is None:
                self.tail = None
            return

        prev_node = self.head
        curr_node = prev_node.next

        while curr_node is not None and curr_node.data != item: #Keep looping thru items until item found
            prev_node = prev_node.next
            curr_node = prev_node.next

        if curr_node is not None and curr_node.data == item:
            prev_node.next = curr_node.next # Skip around node if item found
            if curr_node == self.tail: # Check if item is at tail, adjust pointer if so
                self.tail = prev_node
        else:
            raise ValueError('Item not found: {}'.format(item))


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
