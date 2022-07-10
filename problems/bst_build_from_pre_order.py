from data_structures.tree import TreeNode
from graphviz.tree import TreeDrawer


def build_with_stack(preorder):
    root = TreeNode(preorder[0])
    stack = [root]
    for value in preorder[1:]:
        if value < stack[-1].val:
            stack[-1].left = TreeNode(value)
            stack.append(stack[-1].left)
        else:
            while stack and stack[-1].val < value:
                last = stack.pop()
            last.right = TreeNode(value)
            stack.append(last.right)
    return root


def stack_deneme(preorder):
    root = TreeNode(preorder[0])
    stack = [root]

    for value in preorder[1::]:
        if stack[-1].val > value:
            stack[-1].left = TreeNode(value)
            stack.append(stack[-1].left)
        else:
            while stack and stack[-1].val < value:
                last = stack.pop()
            last.right = TreeNode(value)
            stack.append(last.right)
    return root


if __name__ == "__main__":
    array = [10, 5, 1, 7, 40]
    root = stack_deneme(array)
    TreeDrawer().visualize(root)
    in_order_result = build_with_stack(array)
    print(in_order_result)
