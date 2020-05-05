from data_structures.linked_list.singly_linked_list.node import Node

head = None  # head of list


def segregate_even_odd():
    global head

    # Starting node of list having
    # even values.
    evenStart = None

    # Ending node of even values list.
    evenEnd = None

    # Starting node of odd values list.
    oddStart = None

    # Ending node of odd values list.
    oddEnd = None

    # Node to traverse the list.
    currNode = head

    while (currNode != None):
        val = currNode.data

        # If current value is even, add
        # it to even values list.
        if (val % 2 == 0):
            if (evenStart == None):
                evenStart = currNode
                evenEnd = evenStart
            else:
                evenEnd.next = currNode
                evenEnd = evenEnd.next

        # If current value is odd, add
        # it to odd values list.
        else:
            if (oddStart == None):
                oddStart = currNode
                oddEnd = oddStart
            else:
                oddEnd.next = currNode
                oddEnd = oddEnd.next

        # Move head pointer one step in
        # forward direction
        currNode = currNode.next

        # If either odd list or even list is empty,
    # no change is required as all elements
    # are either even or odd.
    if (oddStart == None or evenStart == None):
        return

    # Add odd list after even list.
    evenEnd.next = oddStart
    oddEnd.next = None

    # Modify head pointer to
    # starting of even list.
    head = evenStart


def push(new_data):
    global head
    # 1 & 2: Allocate the Node &
    #         Put in the data
    new_node = Node(new_data)

    # 3. Make next of new Node as head
    new_node.next = head

    # 4. Move the head to point to new Node
    head = new_node


def print_list():
    global head
    node = head
    while node is not None:
        print(node.data, end=" ")
        node = node.next
    print()


if __name__ == '__main__':
    push(11)
    push(10)
    push(9)
    push(6)
    push(4)
    push(1)
    push(0)

    print("Original Linked list")
    print_list()

    segregate_even_odd()

    print("Modified Linked list")
    print_list()
