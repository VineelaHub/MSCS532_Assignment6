"""
stacks_queues.py
Stack and queue implementations using both arrays and linked lists.
"""

class ArrayStack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


class ArrayQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.items.pop(0)

    def front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListStack:
    def __init__(self):
        self.top = None
        self.count = 0

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node
        self.count += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        value = self.top.data
        self.top = self.top.next
        self.count -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.top.data

    def is_empty(self):
        return self.top is None

    def size(self):
        return self.count


class LinkedListQueue:
    def __init__(self):
        self.front_node = None
        self.rear_node = None
        self.count = 0

    def enqueue(self, value):
        node = Node(value)
        if self.rear_node is None:
            self.front_node = self.rear_node = node
        else:
            self.rear_node.next = node
            self.rear_node = node
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        value = self.front_node.data
        self.front_node = self.front_node.next
        if self.front_node is None:
            self.rear_node = None
        self.count -= 1
        return value

    def front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.front_node.data

    def is_empty(self):
        return self.front_node is None

    def size(self):
        return self.count
