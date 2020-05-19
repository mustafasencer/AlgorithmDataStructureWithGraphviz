from drawer.singly_linked_list import LinkedListDrawer
from data_structures.linked_list.node import Node


def build_linked_list(array):
    head = None
    for item in array[::-1]:
        new_node = Node(item)
        new_node.next = head
        head = new_node
    return head


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5]
    head = build_linked_list(array)
    LinkedListDrawer().visualize(head)
