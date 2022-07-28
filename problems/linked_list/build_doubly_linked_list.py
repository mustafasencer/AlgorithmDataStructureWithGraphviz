from typing import List

from visualization.linked_list import LinkedListDrawer

from data_structures.linked_list import LinkedListNode


def build_linked_list(nums: List[int]) -> LinkedListNode:
    head = None
    for item in nums[::-1]:
        new_node = LinkedListNode(item)
        new_node.next = head
        head = new_node
    return head


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    head = build_linked_list(nums)
    LinkedListDrawer().visualize(head)
