from visualization.base import DiGraphImpl


class TreeDrawer:
    def __init__(self):
        self.digraph = DiGraphImpl(format="png", is_vertical=True)
        self.key_value_pairs = []
        self._key = None
        self.source = None
        self.edges = []

    @property
    def key(self):
        if not self._key:
            self._key = 0
        self._key += 1
        return self._key

    def get_key(self, value):
        key = self.key
        self.key_value_pairs.append((key, value))
        return key

    def get_source(self):
        if self.key_value_pairs:
            key, value = self.key_value_pairs.pop(0)
            self.source = key
            return key
        key = self.key
        self.source = key
        return key

    def create_edges(self):
        for source, destination in self.edges:
            self.digraph.add_edge(source, destination)

    def create_node(self, value):
        source = self.get_source()
        self.digraph.add_node(str(source), str(value) if value is not None else "null")

    def append_edges(self, root):
        if root.left:
            destination = self.get_key(root.left.val)
            self.edges.append((str(self.source), str(destination)))
        if root.right:
            destination = self.get_key(root.right.val)
            self.edges.append((str(self.source), str(destination)))

    def create_nodes(self, root):
        if not root:
            raise ValueError("Tree is empty!")
        _result, queue = [], [root]
        while len(queue) > 0:
            node = queue.pop(0)
            self.create_node(node.val)
            self.append_edges(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        self.create_edges()

    def visualize(self, root):
        self.create_nodes(root)
        self.digraph.view()
