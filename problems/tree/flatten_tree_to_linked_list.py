from visualization.tree import TreeDrawer

from data_structures.tree import TreeNode
from problems.tree.tree_build_level_order import build_tree


def to_linked_list(root):
    result = []
    stack = []
    current = root

    while current or stack:
        if current:
            stack.append(current)
            result.append(current.val)
            current = current.left
        else:
            node = stack.pop()
            current = node.right
    node = None
    for item in result[::-1]:
        new_node = TreeNode(item)
        new_node.next = node
        node = new_node
    return node


def flatten_tree(root):
    stack = []
    current = root
    result = root
    result = TreeNode()
    if not root:
        return

    while current or stack:
        if current:
            stack.append(current)
            if result.val:
                temp = result
                result = TreeNode(current.val)
                result.right = temp
            else:
                result.val = current.val
            current = current.left
            continue
        node = stack.pop()
        current = node.right
    return root


def flatten(root):
    if not root:
        return

    # using Morris Traversal of BT
    node = root

    while node:
        if node.left:
            pre = node.left
            while pre.right:
                pre = pre.right
            pre.right = node.right
            node.right = node.left
            node.left = None
        node = node.right


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7]
    root = build_tree(array, None, 0, len(array))
    result = flatten(root)
    TreeDrawer().visualize(result)
