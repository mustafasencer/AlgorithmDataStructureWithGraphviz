# dfs + stack
from drawer.tree import TreeDrawer
from data_structures.tree.build.level_order import build_tree


def level_order_bottom(root):
    stack = [(root, 0)]
    res = []
    while stack:
        node, level = stack.pop()
        if node:
            if len(res) < level + 1:
                res.insert(0, [])
            res[-(level + 1)].append(node.val)
            stack.append((node.right, level + 1))
            stack.append((node.left, level + 1))
    return res


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5]
    root = build_tree(array, None, 0, len(array))
    result = level_order_bottom(root)
    TreeDrawer().visualize(root)
