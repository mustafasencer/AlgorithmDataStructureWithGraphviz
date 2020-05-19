import time

from data_structures.linked_list.build import build_linked_list
from data_structures.linked_list.node import Node


def insert_nth(head_node, index, data):
    # Your code goes here.
    # Return the head of the list.
    head = head_node
    if not head_node:
        head = Node(data)
        return head
    if index < 1:
        new_node = Node(data)
        new_node.next = head_node
        head = new_node
        return head
    while index > 0:
        if index == 1:
            new_node = Node(data)
            new_node.next = head_node.next
            head_node.next = new_node
            break
        head_node = head_node.next
        index -= 1
    if index != 1:
        print('List index out of range')
    return head


def insert_nth_(head_node, index, data):
    head = head_node
    if not head_node:
        head = head_node
        return head

    if index < 1:
        new_node = Node(data)
        new_node.next = head_node
        head = new_node
        return head

    while index > 0:
        if index == 1:
            new_node = Node(data)
            new_node.next = head_node.next
            head_node.next = new_node
            break
        head_node = head_node.next
        index -= 1
    return head


class __Node(object):
    def __init__(self, data, nxt=None):
        self.data = data
        self.next = nxt


def insert_nth_codewars(head, index, data):
    if index == 0: return __Node(data, head)
    if head and index > 0:
        head.next = insert_nth(head.next, index - 1, data)
        return head
    raise ValueError


def insert_nth__(head, index, data):
    return __Node(data, head) if not index else __Node(head.data, insert_nth__(head.next, index - 1, data))


def print_list(head):
    node = head
    while node is not None:
        print(node.data, end=" -> ")
        node = node.next
    print('NULL')


if __name__ == '__main__':
    INDEX = 3
    VALUE = 100
    RANGE = 5
    head = None
    for i in range(RANGE, 0, -1):
        build_linked_list(i)
    start = time.time()
    result = insert_nth_(head, INDEX, VALUE)
    print_list(result)
    print(time.time() - start)

    print('*********')
