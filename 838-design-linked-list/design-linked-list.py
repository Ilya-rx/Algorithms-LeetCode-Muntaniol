class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index):
        cur = self.head
        for i in range(index):
            if not cur:
                return -1
            cur = cur.next

        return cur.val if cur else -1

    def addAtHead(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node

    def addAtTail(self, val):
        node = Node(val)

        if not self.head:
            self.head = node
            return

        cur = self.head
        while cur.next:
            cur = cur.next

        cur.next = node

    def addAtIndex(self, index, val):
        if index == 0:
            self.addAtHead(val)
            return

        cur = self.head
        for i in range(index - 1):
            if not cur:
                return
            cur = cur.next

        if cur:
            node = Node(val)
            node.next = cur.next
            cur.next = node

    def deleteAtIndex(self, index):
        if index == 0 and self.head:
            self.head = self.head.next
            return

        cur = self.head
        for i in range(index - 1):
            if not cur:
                return
            cur = cur.next

        if cur and cur.next:
            cur.next = cur.next.next