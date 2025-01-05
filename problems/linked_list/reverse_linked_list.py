from data_structures.linked_list import LinkedListNode


def reverse_list(head: LinkedListNode):
    if not head:
        raise ValueError
    result = None
    while head:
        new = LinkedListNode(head.val)
        temp = result
        result = new
        result.next = temp
        head = head.next
    return result


def reverse_list_v2(head: LinkedListNode):
    if not head:
        return None

    result = None

    while head:
        temp = result
        new = LinkedListNode(val=head.val, nxt=temp)
        result = new
        head = head.next

    return result


def print_list(head) -> None:
    node = head
    while node is not None:
        node = node.next


def push(value) -> None:
    global head
    new_node = LinkedListNode(value)
    new_node.next = head
    head = new_node


if __name__ == "__main__":
    head = None
    for i in range(5, 0, -1):
        push(i)
    result = reverse_list_v2(head)

    to_assert = []
    while result:
        to_assert.append(result.val)
        result = result.next

    assert [5, 4, 3, 2, 1] == to_assert
