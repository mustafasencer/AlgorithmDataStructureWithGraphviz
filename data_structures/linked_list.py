class LinkedListNode:
    def __init__(self, val=None, nxt=None) -> None:
        self.val = val
        self.next = nxt


class DoublyLinkedListNode:
    def __init__(self, val=None, nxt=None, prev=None) -> None:
        self.val = val
        self.next = nxt
        self.prev = prev


def print_linked_list(head) -> None:
    node = head
    while node is not None:
        node = node.next
