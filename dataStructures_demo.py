"""
dataStructures_demo.py
Demonstrates all required data structure operations.
"""

from arrays import DynamicArray
from stacks_queues import ArrayStack, ArrayQueue, LinkedListStack, LinkedListQueue
from linked_lists import SinglyLinkedList, TreeNode

def demo_array():
    arr = DynamicArray()
    arr.insert_end(10)
    arr.insert_end(20)
    arr.insert_at(1, 15)
    deleted = arr.delete_at(0)
    return {
        "array_after_operations": arr.traverse(),
        "deleted_value": deleted,
        "access_index_1": arr.access(1)
    }

def demo_stacks():
    a_stack = ArrayStack()
    for x in [1, 2, 3]:
        a_stack.push(x)

    l_stack = LinkedListStack()
    for x in [4, 5, 6]:
        l_stack.push(x)

    return {
        "array_stack_pop": a_stack.pop(),
        "array_stack_peek": a_stack.peek(),
        "linked_stack_pop": l_stack.pop(),
        "linked_stack_peek": l_stack.peek()
    }

def demo_queues():
    a_queue = ArrayQueue()
    for x in ["A", "B", "C"]:
        a_queue.enqueue(x)

    l_queue = LinkedListQueue()
    for x in ["X", "Y", "Z"]:
        l_queue.enqueue(x)

    return {
        "array_queue_dequeue": a_queue.dequeue(),
        "array_queue_front": a_queue.front(),
        "linked_queue_dequeue": l_queue.dequeue(),
        "linked_queue_front": l_queue.front()
    }

def demo_linked_list():
    ll = SinglyLinkedList()
    ll.insert_at_beginning(30)
    ll.insert_at_beginning(20)
    ll.insert_at_end(40)
    ll.insert_after_value(30, 35)
    ll.delete_value(20)
    return {
        "linked_list_values": ll.traverse()
    }

def demo_rooted_tree():
    root = TreeNode("Root")
    child1 = TreeNode("Child-1")
    child2 = TreeNode("Child-2")
    grandchild = TreeNode("Grandchild-1")

    child1.add_child(grandchild)
    root.add_child(child1)
    root.add_child(child2)

    return {
        "tree_preorder": root.preorder()
    }

if __name__ == "__main__":
    print("=== ARRAY DEMO ===")
    print(demo_array())

    print("\n=== STACK DEMO ===")
    print(demo_stacks())

    print("\n=== QUEUE DEMO ===")
    print(demo_queues())

    print("\n=== LINKED LIST DEMO ===")
    print(demo_linked_list())

    print("\n=== ROOTED TREE DEMO ===")
    print(demo_rooted_tree())
