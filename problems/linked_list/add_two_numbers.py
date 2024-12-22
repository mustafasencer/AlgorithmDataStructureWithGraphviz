from data_structures.linked_list import LinkedListNode


def solution(l1, l2):
    carry = 0
    result = cur = LinkedListNode(0)

    while l1 or l2 or carry:
        if l1:
            carry += l1.val
            l1 = l1.next
        if l2:
            carry += l2.val
            l2 = l2.next

        sum = carry % 10
        carry //= 10
        node = LinkedListNode(sum)
        cur.next = node
        cur = cur.next

    return result.next


def push(head, value):
    new_node = LinkedListNode(value)
    new_node.next = head
    return new_node


if __name__ == "__main__":
    l1, l2 = None, None
    for i in [1, 2, 3]:
        l1 = push(l1, i)
    for i in [2, 3, 4]:
        l2 = push(l2, i)
    result = solution(l1, l2)

    while result:
        result = result.next
