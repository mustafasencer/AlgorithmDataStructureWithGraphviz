from data_structures.tree import TreeNode
from visualization.tree import TreeDrawer


def recursive(post_order, in_order):
    if in_order:
        index = in_order.index(post_order.pop())
        root = TreeNode(in_order[index])
        root.right = recursive(post_order, in_order[index + 1 :])
        root.left = recursive(post_order, in_order[:index])
        return root
    return None


def recursive_v2(post_order, in_order):
    map_in_order = {}
    for i, val in enumerate(in_order):
        map_in_order[val] = i

    def recur(low, high):
        if low > high:
            return None
        x = TreeNode(post_order.pop())
        mid = map_in_order[x.val]
        x.right = recur(mid + 1, high)
        x.left = recur(low, mid - 1)
        return x

    return recur(0, len(in_order) - 1)


if __name__ == "__main__":
    in_order = [4, 2, 5, 1, 6, 3, 7]
    post_order = [4, 5, 2, 6, 7, 3, 1]
    root = recursive_v2(post_order, in_order)
    TreeDrawer().visualize(root)
