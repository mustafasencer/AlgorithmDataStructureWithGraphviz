from data_structures.linked_list.singly_linked_list.node import Node


def front_back_split(source, front, back):
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


def print_list(head):
    node = head
    while node is not None:
        print(node.val, end=" -> ")
        node = node.next
    print('NULL')


def push(value):
    global head
    new_node = Node(value)
    new_node.next = head
    head = new_node


if __name__ == '__main__':
    head = None
    front = Node()
    back = Node()
    for i in range(2, 0, -1):
        push(i)
    front, back = front_back_split(head, front, back)
    print_list(front)
    print_list(back)
