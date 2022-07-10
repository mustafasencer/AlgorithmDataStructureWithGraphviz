def is_balanced(root) -> bool:
    def check(root):
        if not root:
            return 0
        left = check(root.left)
        right = check(root.right)
        if right == -1 or left == -1 or abs(left - right) > 1:
            return -1
        return 1 + max(left, right)

    return check(root) != -1


if __name__ == "__main__":
    pass
