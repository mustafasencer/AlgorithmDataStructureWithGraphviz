from data_structures.tree.traversals.dfs_traversals.in_order import stack
from drawer.tree import TreeDrawer
from data_structures.tree.node import Node


def build_with_stack(preorder):
    root = Node(preorder[0])
    stack = [root]
    for value in preorder[1:]:
        if value < stack[-1].val:
            stack[-1].left = Node(value)
            stack.append(stack[-1].left)
        else:
            while stack and stack[-1].val < value:
                last = stack.pop()
            last.right = Node(value)
            stack.append(last.right)
    return root


def stack_deneme(preorder):
    root = Node(preorder[0])
    stack = [root]

    for value in preorder[1::]:
        if stack[-1].val > value:
            stack[-1].left = Node(value)
            stack.append(stack[-1].left)
        else:
            while stack and stack[-1].val < value:
                last = stack.pop()
            last.right = Node(value)
            stack.append(last.right)
    return root


if __name__ == '__main__':
    array = [10, 5, 1, 7, 40]
    root = stack_deneme(array)
    TreeDrawer().visualize(root)
    in_order_result = build_with_stack(array)
    print(in_order_result)
