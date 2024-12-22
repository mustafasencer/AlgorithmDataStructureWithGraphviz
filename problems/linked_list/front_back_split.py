from data_structures.linked_list import LinkedListNode, print_linked_list


def front_back_split(source):
    if not source:
        front = source
        back = None
        return front, back

    slow = source
    fast = source.next

    while fast:
        fast = fast.next
        if not fast:
            break
        slow = slow.next
        fast = fast.next

    front = source
    back = slow.next
    slow.next = None
    return front, back


def push(value) -> None:
    global head
    new_node = LinkedListNode(value)
    new_node.next = head
    head = new_node


if __name__ == "__main__":
    head = None
    for i in range(10, 0, -1):  # construct the linked list by looping in reverse order
        push(i)
    front, back = front_back_split(head)
    print_linked_list(front)
    print_linked_list(back)
