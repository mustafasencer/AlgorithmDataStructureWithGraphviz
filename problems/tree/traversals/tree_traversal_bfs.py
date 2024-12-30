from problems.tree.builds.build_tree_level_order import build_tree
from visualization.tree import TreeDrawer


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


def queue_print_only(root) -> None:
    if root is None:
        return
    queue = [root]

    while len(queue) > 0:
        node = queue.pop(0)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)


def queue_multi_children(root):
    if not root:
        return None
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


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5]
    root = build_tree(array, len(array))
    result = queue(root)
    TreeDrawer().visualize(root)
