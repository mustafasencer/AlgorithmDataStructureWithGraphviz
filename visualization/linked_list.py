from visualization.base import DiGraphImpl


class LinkedListDrawer:
	def __init__(self):
		self.digraph = DiGraphImpl()
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

	def _create_node(self, val):
		key = self.get_key(val)
		self.digraph.add_node(str(key), str(val) if val else "null")

	def _create_edge(self, source, destination):
		self.digraph.add_edge(str(source), str(destination))

	def create_nodes(self, root):
		queue = [root]
		while queue:
			node = queue.pop(0)
			self._create_node(node.val)
			if node.next:
				node = node.next
				queue.append(node)

	def visualize(self, root):
		self.create_nodes(root)
		self.digraph.view()
