"""
https://www.geeksforgeeks.org/inorder-successor-in-binary-search-tree/#:~:text=In%20Binary%20Tree%2C%20Inorder%20successor,key%20of%20the%20input%20node.
"""
from data_structures.tree import TreeNodeWithParent
from problems.tree.bst_build_from_array import build_bst


def solution(node):
    """
    1. if right node does not exist; we need to go to the parent to find the next bigger number
        depending on which child we are coming from:
        left: return parent directly because it is already the smallest possible
        right: we need to go one level above check the upper parent! (tricky part)
    2. if right exists; we need to go to the left most to find the minimum value in the right side! (bst property)
    """
    if not node.right:
        while node.parent:
            p = node.parent
            if p.right != node:
                return p
            node = p
    else:
        return get_min(node.right)
    return None


def get_min(node):
    while node.left:
        node = node.left
    return node


if __name__ == '__main__':
    nums = [1, 3, 2, 4, 2, 5, 7, 6]
    bst = build_bst(nums)
    result = solution(bst)
    assert result == TreeNodeWithParent()
