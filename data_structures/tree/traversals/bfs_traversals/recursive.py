# dfs recursively
from data_structures.tree.build.level_order import build_tree


def level_order_bottom(root):
    res = []
    dfs(root, 0, res)
    return res


def dfs(root, level, res):
    if root:
        if len(res) < level + 1:
            res.insert(0, [])
        res[-(level + 1)].append(root.val)
        dfs(root.left, level + 1, res)
        dfs(root.right, level + 1, res)


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5]
    root = build_tree(array, None, 0, len(array))
    result = level_order_bottom(root)
    print(result)
