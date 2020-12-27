'''
Linked List Practice
Implement a linked list class. You have to define a few functions that perform the desirbale action. Your LinkedList class should be able to:

Append data to the tail of the list and prepend to the head
Search the linked list for a value and return the node
Remove a node
Pop, which means to return the first node's value and delete the node from the list
Insert data at some position in the list
Return the size (length) of the linked list
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out


# Define a function outside of the class
def prepend(self, value):
    """ Prepend a value to the beginning of the list. """
    # TODO: Write function to prepend here
    new_node = Node(value)
    if self.head:
        new_node.next = self.head
    self.head = new_node


# This is the way to add a function to a class after it has been defined
LinkedList.prepend = prepend

# Test prepend
linked_list = LinkedList()
linked_list.prepend(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"

def append(self, value):
    """ Append a value to the end of the list. """
    # TODO: Write function to append here
    new_node = Node(value)
    if self.head is None:
        self.head = new_node
    else:
        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

LinkedList.append = append

# Test append - 1
linked_list.append(3)
linked_list.prepend(2)
assert linked_list.to_list() == [2, 1, 3], f"list contents: {linked_list.to_list()}"

# Test append - 2
linked_list = LinkedList()
linked_list.append(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
assert linked_list.to_list() == [1, 3], f"list contents: {linked_list.to_list()}"

def search(self, value):
    """ Search the linked list for a node with the requested value and return the node. """
    # TODO: Write function to search here
    current_node = self.head
    while current_node:
        if current_node.value == value:
            return current_node
        else:
            current_node = current_node.next
    return None

LinkedList.search = search

# Test search
linked_list.prepend(2)
linked_list.prepend(1)
linked_list.append(4)
linked_list.append(3)
assert linked_list.search(1).value == 1, f"list contents: {linked_list.to_list()}"
assert linked_list.search(4).value == 4, f"list contents: {linked_list.to_list()}"

def remove(self, value):
    """ Remove first occurrence of value. """
    # TODO: Write function to remove here
    current_node = self.head
    if current_node.value == value:
        self.head = current_node.next
    else:
        while current_node:
            if current_node is None:
                return
            elif current_node.next.value == value:
                 current_node.next = current_node.next.next
                 return
            else:
                current_node = current_node.next

LinkedList.remove = remove

# Test remove
linked_list.remove(1)
assert linked_list.to_list() == [2, 1, 3, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4], f"list contents: {linked_list.to_list()}"


def pop(self):
    """ Return the first node's value and remove it from the list. """
    # TODO: Write function to pop here
    if self.head is None:
        return None

    head = self.head
    self.head = self.head.next
    return head.value


LinkedList.pop = pop

# Test pop
value = linked_list.pop()
assert value == 2, f"list contents: {linked_list.to_list()}"
assert linked_list.head.value == 1, f"list contents: {linked_list.to_list()}"


def insert(self, value, pos):
    """ Insert value at pos position in the list. If pos is larger than the
    length of the list, append to the end of the list. """

    # TODO: Write function to insert here
    current_node = self.head
    to_insert = Node(value)
    current_pos = 0
    if pos == 0:
        to_insert.next = self.head
        self.head = to_insert
    else:
        while current_pos < pos - 1 and current_node.next is not None:
            current_node = current_node.next
            current_pos += 1

        to_insert.next = current_node.next
        current_node.next = to_insert


LinkedList.insert = insert

# Test insert
linked_list.insert(5, 0)
assert linked_list.to_list() == [5, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(2, 1)
assert linked_list.to_list() == [5, 2, 1, 4], f"list contents: {linked_list.to_list()}"
linked_list.insert(3, 6)
assert linked_list.to_list() == [5, 2, 1, 4, 3], f"list contents: {linked_list.to_list()}"

def size(self):
    """ Return the size or length of the linked list. """
    # TODO: Write function to get size here
    size =0
    current_node = self.head
    while current_node:
        size +=1
        current_node = current_node.next
    return size

LinkedList.size = size

assert linked_list.size() == 5, f"list contents: {linked_list.to_list()}"