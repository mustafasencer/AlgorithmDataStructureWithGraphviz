from problems.tree.tree_build_level_order import build_tree


def complete_binary_tree(a):
    root = None
    result = []
    root = build_tree(a, root, 0, len(a))
    print_inorder(root, result)
    return result


def print_inorder(root, result) -> None:
    if root:
        print_inorder(root.left, result)

        result.append(root.val)

        print_inorder(root.right, result)


def build_tree_from_inorder(array, start, end):
    if start > end:
        return None

        if inStrt == inEnd:
            return tNode

        inIndex = search(inOrder, inStrt, inEnd, tNode.data)

        tNode.left = buildTree(inOrder, preOrder, inStrt, inIndex - 1)
        tNode.right = buildTree(inOrder, preOrder, inIndex + 1, inEnd)

        return tNode
    return None


if __name__ == "__main__":
    input = [1, 2, 3, 4, 5, 6]
    result = complete_binary_tree(input)
