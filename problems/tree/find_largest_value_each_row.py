from problems.tree.builds.build_tree_level_order import build_tree


def largest_value(root):
    result, level = [root.val], [root]
    while level:
        pairs = [(node.left, node.right) for node in level]
        level = [leaf for pair in pairs for leaf in pair if leaf]
        if level:
            values = [row.val for row in level if row.val is not None]
            result.append(max(values))
    return result


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, None, 6]
    root = build_tree(array, None, 0, len(array))
    result = largest_value(root)
