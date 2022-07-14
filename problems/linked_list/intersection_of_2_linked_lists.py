from data_structures.linked_list import LinkedListNode
from problems.linked_list.build_linked_list import build_linked_list


def get_intersection_node(headA: LinkedListNode, headB: LinkedListNode):
    count_a = get_count(headA)
    count_b = get_count(headB)
    if count_a > count_b:
        d = count_a - count_b
        get_intersection(d, headA, headB)
    if count_b > count_a:
        d = count_b - count_a
        get_intersection(d, headB, headA)


def get_intersection(d, Node1, Node2):
    current1 = Node1
    current2 = Node2
    for i in range(d):
        if Node1 is None:
            return -1
        current1 = current1.next
    while current1 is not None and current2 is not None:
        if current1.val == current2.val:
            return current1.val
        current1 = current1.next
        current2 = current2.next
    return -1


def get_count(node: LinkedListNode):
    count = 0
    while node.next is not None:
        count += 1
        node = node.next
    return count


if __name__ == "__main__":
    nums = [4, 1, 8, 4, 5]
    node_a = build_linked_list(nums)

    nums = [5, 0, 1, 8, 4, 5]
    node_b = build_linked_list(nums)

    get_intersection_node(node_a, node_b)
