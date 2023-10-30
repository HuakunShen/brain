from DataStructure.Node import *


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def enqueue_head(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

    def dequeue(self):
        if self.head is not None:
            first = self.head
            self.head = self.head.next
            return first.value
        else:
            return None

    def is_empty(self):
        return self.head is None

    def clear(self):
        self.head = None
        self.tail = None

    def __str__(self):
        result = ''
        curr = self.head
        while curr is not None:
            result += ', ' + str(curr.value)
            curr = curr.next
        return result
