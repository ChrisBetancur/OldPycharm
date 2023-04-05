class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def addNode(head, data):
    if head is None:
        head = Node(data)
        return;

    currNode = head;

    while currNode.next is not None:
        currNode = currNode.next

    currNode.next = Node(data)


def deleteNode(head, data):
    currNode = head

    if head.data is data:
        currNode = currNode.next
        return

    prev = None

    while currNode is not None:
        if currNode.data == data:
            prev.next = currNode.next

        prev = currNode
        currNode = currNode.next


def printLinkedList(head):
    currNode = head
    while currNode is not None:
        print(currNode.data)
        currNode = currNode.next


head = Node(5)

addNode(head, 4)
addNode(head, 9)
addNode(head, 2)
deleteNode(head, 5)
printLinkedList(head)
