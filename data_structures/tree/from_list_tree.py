from data_structures.tree.node import Node

a = [3, 9, 20, None, None, 15, 7, 12, 10, None]
b = [1, 2, 2, 3, 3, None, None, 4, 4]
c = [3, 9, 20, None, None, 15, 7]


def from_list_to_tree(nums):
    mid = len(nums) // 2
    root = Node(nums[mid])
    root.left = from_list_to_tree(nums[:mid])
    root.right = from_list_to_tree(nums[mid + 1:])
    return root


from_list_to_tree([1, 2, 3, 4, 5, 6])
