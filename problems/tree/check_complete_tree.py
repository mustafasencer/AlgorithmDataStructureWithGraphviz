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
    array = [1, None, 1, 3, None, 5]
    root = build_tree(array, None, 0, len(array))
    result = solution(root)
    TreeDrawer().visualize(root)
