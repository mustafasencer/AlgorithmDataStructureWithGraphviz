from drawer.my_digraph import MyDiGraph


class LinkedListDrawer:
    def __init__(self):
        self.digraph = MyDiGraph()

    def _create_node(self, val):
        self.digraph.add_node(str(val), str(val) if val else 'null')

    def _create_edge(self, source, destination):
        self.digraph.add_edge(str(source), str(destination))

    def create_nodes(self, root):
        if root and root.val:
            self._create_node(root.val)
            if root.next and root.next.val:
                self._create_edge(root.val, root.next.val)
            self.create_nodes(root.next)

    def visualize(self, root):
        self.create_nodes(root)
        self.digraph.view()
