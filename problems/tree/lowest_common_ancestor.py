from problems.tree.builds.build_tree_level_order import build_tree
from visualization.tree import TreeDrawer


def recursive(root, p, q):
    if root in (p, q) or root is None:
        return root

    # Find p/q in left subtree
    _list = recursive(root.left, p, q)

    # Find p/q in right subtree
    r = recursive(root.right, p, q)

    # If p and q found in left and right subtree of this node, then this node is LCA
    if _list and r:
        return root

    # Else return the node which returned a node from it's subtree such that one of it's ancestor will be LCA
    return _list if _list else r


def lowest_common_ancestor(root):
    def helper(root):
        if not root:
            return 0, None
        h1, lca1 = helper(root.left)
        h2, lca2 = helper(root.right)
        if h1 > h2:
            return h1 + 1, lca1
        if h1 < h2:
            return h2 + 1, lca2
        return h1 + 1, root

    return helper(root)[1]


def trial(root):
    def helper(root):
        if not root:
            return 0, None
        hl, lcal = helper(root.left)
        hr, lcar = helper(root.right)
        if hl > hr:
            return hl + 1, lcal
        if hr > hl:
            return hr + 1, lcar
        return hl + 1, root

    return helper(root)[1]


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, None, 13, 14]
    root = build_tree(array, None, 0, len(array))
    result = trial(root)
    TreeDrawer().visualize(result)
