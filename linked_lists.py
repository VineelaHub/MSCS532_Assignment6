"""
linked_lists.py
Singly linked list and optional rooted tree implementation.
"""

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, value):
        node = ListNode(value)
        node.next = self.head
        self.head = node

    def insert_at_end(self, value):
        node = ListNode(value)
        if self.head is None:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node

    def insert_after_value(self, target, value):
        current = self.head
        while current:
            if current.data == target:
                node = ListNode(value)
                node.next = current.next
                current.next = node
                return
            current = current.next
        raise ValueError("Target value not found")

    def delete_value(self, value):
        if self.head is None:
            raise ValueError("List is empty")

        if self.head.data == value:
            self.head = self.head.next
            return

        prev = None
        current = self.head
        while current and current.data != value:
            prev = current
            current = current.next

        if current is None:
            raise ValueError("Value not found")

        prev.next = current.next

    def traverse(self):
        values = []
        current = self.head
        while current:
            values.append(current.data)
            current = current.next
        return values


class TreeNode:
    """
    Optional rooted tree using linked lists.
    Each node stores a value and a linked-list style list of children references.
    """
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def preorder(self):
        result = [self.value]
        for child in self.children:
            result.extend(child.preorder())
        return result
