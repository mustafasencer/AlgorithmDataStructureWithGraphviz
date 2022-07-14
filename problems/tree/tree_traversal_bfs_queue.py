from visualization.tree import TreeDrawer

from problems.tree.tree_build_level_order import build_tree


def queue_bottom_with_level(root):
    queue, res = [(root, 0)], []
    while queue:
        node, level = queue.pop(0)
        if node:
            if len(res) < level + 1:
                res.insert(0, [])
            res[-(level + 1)].append(node.val)
            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))
    return res


def queue_multi_children(root):
    if not root:
        return
    result, queue = [root.val], [[root]]
    while len(queue) > 0:
        nodes = queue.pop(0)
        if nodes:
            for node in nodes:
                if node.child_nodes:
                    for child in node.child_nodes:
                        result.append(child.val)
                        queue.append(child.child_nodes)
                else:
                    result.append(node.val)
    return result


def queue(root):
    if not root:
        return []
    result, queue = [], [root]

    while len(queue) > 0:
        node = queue.pop(0)
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


def queue_with_level(root):
    result, level = [], [root]

    while root and level:
        result.extend([node.data for node in level])
        pairs = [(node.left, node.right) for node in level]
        level = [leaf for pair in pairs for leaf in pair if leaf]
    return result


def print_queue(root):
    if root is None:
        return
    queue = [root]

    while len(queue) > 0:
        print(queue[0].val)
        node = queue.pop(0)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5]
    root = build_tree(array, None, 0, len(array))
    result = queue_bottom_with_level(root)
    TreeDrawer().visualize(root)
