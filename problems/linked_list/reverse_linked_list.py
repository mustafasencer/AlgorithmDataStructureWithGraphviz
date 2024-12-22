from data_structures.linked_list import LinkedListNode


def reverse_list(node):
	if not node:
		raise ValueError
	result = None
	while node:
		new = LinkedListNode(node.data)
		temp = result
		result = new
		result.next = temp
		node = node.next
	return result


def print_list(head):
	node = head
	while node is not None:
		print(node.data, end=" -> ")
		node = node.next
	print("NULL")


def push(value):
	global head
	new_node = LinkedListNode(value)
	new_node.next = head
	head = new_node


if __name__ == "__main__":
	head = None
	for i in range(5, 0, -1):
		push(i)
	reverse_list(head)
