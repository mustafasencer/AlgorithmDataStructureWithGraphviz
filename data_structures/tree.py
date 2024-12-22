class TreeNode:
    def __init__(self, val=None) -> None:
        self.left = None
        self.right = None
        self.val = val


class TreeNodeWithParent:
    def __init__(self, val=None) -> None:
        self.left = None
        self.right = None
        self.parent = None
        self.val = val


class TreeNodeWithChildren:
    def __init__(self, data, child_nodes=None) -> None:
        self.data = data
        self.child_nodes = child_nodes
