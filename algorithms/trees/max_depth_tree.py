from data_structures.tree.node import Node


class Solution:
    bi_graph = None
    left_counter = 0
    right_counter = 0

    class GraphAttributes:
        name = 'OTA'
        label = """<<FONT POINT-SIZE="30" FACE="ubuntu">OTA: {}</FONT><BR ALIGN="CENTER"/>>"""
        rankdir = 'LR'

    class NodeAttributes:
        node_label = """<<FONT POINT-SIZE="18" FACE="ubuntu">{}</FONT><BR ALIGN="CENTER"/>>"""

    def max_depth(self, root: Node) -> int:
        if not root:
            return 0
        return 1 + max(self.max_depth(root.left), self.max_depth(root.right))
