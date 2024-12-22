from problems.tree.tree_build_level_order import build_tree


def level_order_bottom_recursion(root):
    res = []
    dfs(root, 0, res)
    return res


def dfs(root, level, res) -> None:
    if not root:
        return
    if len(res) < level + 1:
        res.insert(0, [])
    res[-(level + 1)].append(root.val)
    dfs(root.left, level + 1, res)
    dfs(root.right, level + 1, res)


def level_order_bottom_stack(root):
    stack = [(root, 0)]
    res = []
    while stack:
        node, level = stack.pop()
        if not node:
            continue

        if len(res) < level + 1:
            res.insert(0, [])
        res[-(level + 1)].append(node.val)
        stack.append((node.right, level + 1))
        stack.append((node.left, level + 1))
    return res


def queue_bottom_with_level_bfs_queue(root):
    queue, res = [(root, 0)], []
    while queue:
        node, level = queue.pop(0)
        if not node:
            continue

        if len(res) < level + 1:
            res.insert(0, [])
        res[-(level + 1)].append(node.val)
        queue.append((node.left, level + 1))
        queue.append((node.right, level + 1))
    return res


def queue_with_level(root):
    result, level = [], [root]

    while root and level:
        result.extend([node.val for node in level])
        pairs = [(node.left, node.right) for node in level]
        level = [leaf for pair in pairs for leaf in pair if leaf]
    return result


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5]
    root = build_tree(array, None, 0, len(array))
    result = queue_with_level(root)
    assert result == [[4, 5], [2, 3], [1]]
