class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    """Return Linked List union of two
    Args:
        llist_1: linked list
        llist_2: linked list
    Returns:
        linked_list_un: union of input Linked List
    """
    linked_list_un = LinkedList()
    node = llist_1.head
    while node:
        node_to_append = Node(node.value)
        linked_list_un.append(node_to_append)
        node = node.next

    node = llist_2.head
    while node:
        node_to_append = Node(node.value)
        linked_list_un.append(node_to_append)
        node = node.next

    return linked_list_un


def intersection(llist_1, llist_2):
    """Return Linked List union of two
    Args:
        llist_1: linked list
        llist_2: linked list
    Returns:
        linked_list_un: intersection of input Linked List
    """
    in_first = set()
    node = llist_1.head
    while node:
        in_first.add(node.value)
        node = node.next

    linked_list_in = LinkedList()

    node = llist_2.head

    while node:
        if node.value in in_first:
            node_to_append = Node(node.value)
            linked_list_in.append(node_to_append)
        node = node.next

    return linked_list_in


if __name__ == "__main__":
    # Test case 1
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,21]
    element_2 = [6,32,4,9,6,1,11,21,1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print(f'union list is {union(linked_list_1,linked_list_2)}')
    print(f'intersection list is {intersection(linked_list_1,linked_list_2)}')

    # Test case 2
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,23]
    element_2 = [1,7,8,9,11,21,1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print(f'union list is {union(linked_list_3, linked_list_4)}')
    print(f'intersection list is {intersection(linked_list_3, linked_list_4)}')

    # Test case 3
    linked_list_5 = LinkedList()
    linked_list_6 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
    element_2 = []

    for i in element_1:
        linked_list_5.append(i)

    for i in element_2:
        linked_list_6.append(i)

    print(f'union list is {union(linked_list_5, linked_list_6)}')# expected list like list 1
    print(f'intersection list is {intersection(linked_list_5, linked_list_6)}') # expected empty list

    # Test case 4
    linked_list_7 = LinkedList()
    linked_list_8 = LinkedList()

    element_1 = []
    element_2 = []

    for i in element_1:
        linked_list_5.append(i)

    for i in element_2:
        linked_list_6.append(i)

    print(f'union list is {union(linked_list_7, linked_list_8)}') # expected empty list
    print(f'intersection list is {intersection(linked_list_7, linked_list_8)}')# expected empty list