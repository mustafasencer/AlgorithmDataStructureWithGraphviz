from visualization.tree import TreeDrawer

from data_structures.tree import TreeNode


def build_bst(nums):
    if not nums:
        return None
    nums = [i for i in nums if i is not None]

    nums.sort()

    # find middle
    mid = int((len(nums)) / 2)

    # make the middle element the root
    root = TreeNode(nums[mid])

    # left subtree of root has all
    # values <arr[mid]
    root.left = build_bst(nums[:mid])

    # right subtree of root has all
    # values >arr[mid]
    root.right = build_bst(nums[mid + 1:])
    return root


if __name__ == "__main__":
    nums = [1, 3, 5, 4, 2, 6, 7]
    root = build_bst(nums)
    TreeDrawer().visualize(root)
