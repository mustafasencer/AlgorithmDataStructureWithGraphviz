from data_structures.tree import TreeNode
from graphviz.linked_list import LinkedListDrawer


def build_linked_list(nums):
    head = None
    for item in nums[::-1]:
        new_node = TreeNode(item)
        new_node.next = head
        head = new_node
    return head


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    head = build_linked_list(nums)
    LinkedListDrawer().visualize(head)
