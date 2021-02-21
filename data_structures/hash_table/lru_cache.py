from functools import lru_cache


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
    def remove_dlink(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    # head <->  nxt
    def add_dlink(self, node):
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

            return node.value
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
            node.value = value
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


if __name__ == '__main__':
    capacity = 50
    obj = LRUCache(capacity)
    for i in range(100):
        obj.put(i % 10, 20)

    obj.get(20)
    obj.get(30)
