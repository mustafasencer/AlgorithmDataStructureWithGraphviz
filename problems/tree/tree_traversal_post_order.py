from data_structures.tree import TreeNode
from problems.tree.tree_build_level_order import build_tree
from visualization.tree import TreeDrawer


def recursive(root, p, q):  # post order recursive traversal
	result = []

	def helper(root):
		if root:
			helper(root.left)
			helper(root.right)
			result.append(root.val)

	helper(root)
	return result


def stack(root):
	current = root
	stack = []
	result = TreeNode()
	if not root:
		return []
	while stack or current:
		if current:
			stack.append(current)
			if result.val:
				temp = result
				result = TreeNode(current.val)
				result.next = temp
			else:
				result.val = current.val
			current = current.right
		else:
			node = stack.pop()
			current = node.left
	result_ = []
	while result:
		result_.append(result.val)
		result = result.next
	return result_


if __name__ == "__main__":
	array = [1, 2, 3, 4, 5, 6, 7]
	root = build_tree(array, None, 0, len(array))
	result = stack(root)
	TreeDrawer().visualize(root)
	print(result)
