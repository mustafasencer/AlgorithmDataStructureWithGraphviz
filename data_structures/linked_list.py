class LinkedListNode:
	def __init__(self, val=None, nxt=None):
		self.val = val
		self.next = nxt


class DoublyLinkedListNode:
	def __init__(self, val=None, nxt=None, prev=None):
		self.val = val
		self.next = nxt
		self.prev = prev


def print_linked_list(head):
	node = head
	while node is not None:
		print(node.val, end=" -> ")
		node = node.next
	print("NULL")
