"""
arrays.py
Basic array-based operations implemented using Python lists.
"""

class DynamicArray:
    def __init__(self):
        self.data = []

    def insert_end(self, value):
        self.data.append(value)

    def insert_at(self, index, value):
        if index < 0 or index > len(self.data):
            raise IndexError("Index out of range")
        self.data.insert(index, value)

    def delete_at(self, index):
        if index < 0 or index >= len(self.data):
            raise IndexError("Index out of range")
        return self.data.pop(index)

    def access(self, index):
        if index < 0 or index >= len(self.data):
            raise IndexError("Index out of range")
        return self.data[index]

    def traverse(self):
        return [item for item in self.data]

    def __len__(self):
        return len(self.data)

    def __str__(self):
        return str(self.data)
