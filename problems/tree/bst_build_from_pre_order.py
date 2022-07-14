from visualization.tree import TreeDrawer

from data_structures.tree import TreeNode


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


if __name__ == "__main__":
    nums = [10, 5, 1, 7, 40]
    root = build_with_stack(nums)
    TreeDrawer().visualize(root)
    in_order_result = build_with_stack(nums)
    print(in_order_result)
