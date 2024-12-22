from graphviz import Digraph


class DiGraphImpl:
    class GraphAttributes:
        label = """<<FONT POINT-SIZE="30" FACE="ubuntu">{}</FONT><BR ALIGN="CENTER"/>>"""

    class NodeAttributes:
        node_label = """<<FONT POINT-SIZE="18" FACE="ubuntu">%s</FONT><BR ALIGN="CENTER"/>>"""

    def __init__(self, name="", format="pdf", is_vertical=False):
        self.digraph = Digraph(format=format)
        self.digraph.attr(name=name, rankdir="TB" if is_vertical else "LR")

    def add_node(self, key, value):
        if value == "null":
            self.digraph.node(
                key,
                DiGraphImpl.NodeAttributes.node_label % value,
                shape="point",
                width=".2",
                height=".2",
            )

        else:
            self.digraph.node(
                key,
                DiGraphImpl.NodeAttributes.node_label % value,
                shape="circle",
                width="1",
                height="1",
            )

    def add_edge(self, source, destination):
        self.digraph.edge(source, destination)

    def view(self):
        self.digraph.view()
