from data_structures.linked_list.node import Node


class Solution:
    def odd_even_list(self, head: Node):
        count_total = self.get_count(head)
        count = 1
        current = head.next
        while current.next:
            temp = current
            current = current.next
            current.next = temp
            count += 1

    def get_count(self, head: Node) -> int:
        count = 0
        while head.next != None:
            head = head.next
            count += 1
        return count


class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second


class LinkedList:
    def __init__(self):
        self.head = None

    def rearrange_odd_even(self):

        # Corner case
        if self.head is None:
            return None

        odd = self.head
        even = self.head.next

        even_first = even

        while True:

            if (odd is None or even is None) or even.next is None:
                odd.next = even_first
                break

            # Connecting odd nodes
            odd.next = even.next
            odd = even.next

            if odd.next is None:
                even.next = None
                odd.next = even_first
                break

            # Connecting even nodes
            even.next = odd.next
            even = odd.next
        return self.head

    def deneme(self):
        if not self.head or not self.head.next:
            raise ValueError
        odd = self.head
        even = self.head.next

        even_first = even

        while True:
            if not odd or not even or not odd.next:
                return Context(self.head, even_first)
            odd.next = even.next
            odd = odd.next
            if not odd:
                return Context(self.head, even_first)
            even.next = odd.next
            even = even.next

    def print_list(self, node):
        while (node != None):
            print(node.data, end="")
            print("->", end="")
            node = node.next
        print("NULL")

        # Function to insert a new node

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


if __name__ == '__main__':
    ll = LinkedList()
    # ll.push(7)
    # ll.push(6)
    # ll.push(5)
    # ll.push(4)
    # ll.push(3)
    # ll.push(2)
    ll.push(1)
    print("Given Linked List")
    ll.print_list(ll.head)

    context = ll.deneme()

    print("\nModified Linked List")
    # ll.print_list(start)
