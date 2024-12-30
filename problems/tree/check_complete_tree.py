from problems.tree.builds.build_tree_level_order import build_tree
from visualization.tree import TreeDrawer


def solution(root) -> bool:
    if not root:
        return False

    queue = [root]
    level = 0

    while queue[level] and queue[level].val:
        queue.append(queue[level].left)
        queue.append(queue[level].right)
        level += 1
    return not any(queue[level:])


if __name__ == "__main__":
    array = [1, 2, 3, 4, None, 5]
    root = build_tree(array, len(array))
    result = solution(root)
    assert result is False
    TreeDrawer().visualize(root)
