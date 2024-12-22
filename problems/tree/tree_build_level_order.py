from data_structures.tree import TreeNode


def build_tree(array, root, i, n) -> TreeNode:
	if i < n:
		new_node = TreeNode(array[i])
		root = new_node
		root.left = build_tree(array, root.left, 2 * i + 1, n)
		root.right = build_tree(array, root.right, 2 * i + 2, n)

	return root
