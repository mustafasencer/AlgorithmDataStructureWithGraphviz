from graphviz.tree import TreeDrawer
from problems.tree_build_level_order import build_tree


def check_completeness(root):
    if not root:
        return False

    queue = [root]
    level = 0

    while queue:
        queue.pop(0)
        queue.append(queue[level].left)
        queue.append(queue[level].right)
        level += 1
    return not any(queue[level::])


def test(root):
    if not root:
        return False

    queue = [root]
    node_index = 0

    while queue[node_index] and queue[node_index].val:
        queue.append(queue[node_index].left)
        queue.append(queue[node_index].right)
        node_index += 1
    return not any(queue[node_index:])


if __name__ == "__main__":
    array = [1, None, 1, 3, None, 5]
    root = build_tree(array, None, 0, len(array))
    result = test(root)
    TreeDrawer().visualize(root)
    print(result)
