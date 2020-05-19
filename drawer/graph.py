"""
    Created by Mustafa Sencer Özcan on 18.05.2020.
"""
from drawer.my_digraph import MyDiGraph


class GraphDrawer:
    def __init__(self):
        self.digraph = MyDiGraph(format='png')
        self.key_value_pairs = []
        self._key = None
        self.source = None
        self.edges = []

    def create_nodes(self, graph):
        if not root:
            raise ValueError('Tree is empty!')
        result, queue = [], [root]
        while len(queue) > 0:
            node = queue.pop(0)
            self.create_node(node.val)
            self.append_edges(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        self.create_edges()

    def visualize(self, graph):
        self.create_nodes(graph)
        self.digraph.view()


if __name__ == '__main__':
    array = [1, 2, 1, 8, 5, 6, 7, 4, 6, 4, 6, 3, 5]
    root = build_graph(array, None, 0, len(array))
    drawer = GraphDrawer()
    drawer.visualize(root)
