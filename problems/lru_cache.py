from collections import OrderedDict


class DLinkNode:
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.prev = None
		self.next = None


class LRUCache:
	def __init__(self, capacity):
		"""
		:type capacity: int
		"""
		self.capacity = capacity

		self.lookup = {}  # value to LNode

		# double linked list, support delete
		self.head, self.tail = DLinkNode(0, 0), DLinkNode(0, 0)
		self.head.next = self.tail
		self.tail.prev = self.head

	# remove  node <-> target <-> node
	def remove_link(self, node):
		node.prev.next = node.next
		node.next.prev = node.prev

	# head <->  nxt
	def add_link(self, node):
		# o -> o -> o -> o -> None
		nxt = self.head.next

		self.head.next = node

		node.prev = self.head
		node.next = nxt

		nxt.prev = node

	# get and update
	def get(self, key):
		"""
		:type key: int
		:rtype: int
		"""
		if key in self.lookup:
			node = self.lookup[key]
			# update
			self.remove_dlink(node)
			self.add_dlink(node)

			return node.data
		else:
			return -1

	# head <-> node
	def put(self, key, value):
		"""
		:type key: int
		:type value: int
		:rtype: None
		"""

		# exist: update value and update state
		# non exist: create new node, add to lookup and add to linked list

		if key in self.lookup:
			# change the value and update state
			node = self.lookup[key]
			# change
			node.data = value
			# update
			self.remove_dlink(node)
			self.add_dlink(node)
		else:
			# add new node
			node = DLinkNode(key, value)
			# check capacity
			if len(self.lookup) >= self.capacity:
				temp_node = self.tail.prev
				self.remove_dlink(temp_node)
				del self.lookup[temp_node.key]

			self.lookup[key] = node
			self.add_dlink(node)


class LRUCacheDict:
	def __init__(self, size=10):
		self.size = size
		self.cache = OrderedDict()

	def get(self, key):
		try:
			value = self.cache.pop(key)
		except KeyError:
			return -1
		self.cache[key] = value
		return value

	def set(self, key, value):
		try:
			self.cache.pop(key)
		except KeyError:
			if len(self.cache) >= self.size:
				self.cache.popitem()
		self.cache[key] = value


if __name__ == "__main__":
	capacity = 50
	obj = LRUCache(capacity)
	for i in range(100):
		obj.put(i % 10, 20)

	obj.get(20)
	obj.get(30)
