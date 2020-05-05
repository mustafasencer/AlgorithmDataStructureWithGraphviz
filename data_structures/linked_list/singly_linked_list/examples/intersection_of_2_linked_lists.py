from data_structures.linked_list.singly_linked_list.node import Node


class Solution:
    def get_intersection_node(self, headA: Node, headB: Node) -> Node:
        count_a = self.get_count(headA)
        count_b = self.get_count(headB)
        if count_a > count_b:
            d = count_a - count_b
            self.get_intersection(d, headA, headB)
        if count_b > count_a:
            d = count_b - count_a
            self.get_intersection(d, headB, headA)

    def get_intersection(self, d, Node1, Node2):
        current1 = Node1
        current2 = Node2
        for i in range(d):
            if Node1 is None:
                return -1
            current1 = current1.next
        while current1 is not None and current2 is not None:
            if current1.val == current2.val:
                return current1.val
            current1 = current1.next
            current2 = current2.next
        return -1

    def get_count(self, node: Node):
        count = 0
        while node.next != None:
            count += 1
            node = node.next
        return count


if __name__ == '__main__':
    node_a = Node(4)
    node_a.next = Node(1)
    node_a.next.next = Node(8)
    node_a.next.next.next = Node(4)
    node_a.next.next.next.next = Node(5)

    node_b = Node(5)
    node_b.next = Node(0)
    node_b.next.next = Node(1)
    node_b.next.next.next = Node(8)
    node_b.next.next.next.next = Node(4)
    node_b.next.next.next.next.next = Node(5)

    Solution().get_intersection_node(node_a, node_b)
