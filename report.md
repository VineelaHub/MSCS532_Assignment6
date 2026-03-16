# PART-1: Implementation and Analysis of Selection Algorithms

## Introduction

The order statistics problem focuses on finding the k-th smallest
element in an unsorted array. Efficient solutions to this problem are
important in many applications such as statistics, data analysis,
database systems, and real‑time processing systems.

This project implements and compares two algorithms for solving the
selection problem:

-   Deterministic Selection using the Median of Medians algorithm
-   Randomized Selection using the Quickselect algorithm

The deterministic algorithm guarantees linear time in the worst case,
while the randomized algorithm achieves linear time in expectation. This
report explains the implementation, theoretical analysis, and empirical
evaluation of both algorithms.

------------------------------------------------------------------------

## Algorithm Implementations

### Deterministic Selection (Median of Medians)

The deterministic selection algorithm ensures worst‑case linear time by
carefully choosing a pivot that guarantees balanced partitioning.

Steps: 1. Divide the array into groups of five elements. 2. Find the
median of each group. 3. Recursively compute the median of these
medians. 4. Use this median as the pivot. 5. Partition the array around
the pivot. 6. Recursively select in the relevant partition.

This pivot selection ensures that a constant fraction of elements are
discarded in each recursion.

### Randomized Selection (Quickselect)

Randomized Quickselect is based on the partitioning strategy of
Quicksort.

Steps: 1. Choose a random pivot from the array. 2. Partition the array
into three parts: - elements less than pivot - elements equal to pivot -
elements greater than pivot 3. Determine which partition contains the
k-th element. 4. Recurse only into that partition.

This approach avoids sorting the entire array and typically performs
very efficiently.

------------------------------------------------------------------------

## Time Complexity Analysis

### Deterministic Selection

The recurrence relation for the deterministic selection algorithm is:

T(n) = T(n/5) + T(7n/10) + O(n)

Explanation: - T(n/5) corresponds to computing the median of medians. -
T(7n/10) corresponds to recursion on the larger partition. - O(n)
represents the cost of partitioning and computing medians.

Solving this recurrence gives:

Worst‑case time complexity = O(n)

This makes the algorithm particularly useful when guaranteed performance
is required.

### Randomized Selection

The randomized algorithm has the recurrence:

T(n) = T(n/2) + O(n)

On average, a random pivot divides the array roughly in half. Therefore:

Expected time complexity = O(n)

Worst‑case time complexity = O(n²), but this case is extremely unlikely
with random pivot selection.

------------------------------------------------------------------------

## Space Complexity

Both algorithms require additional memory due to recursion.

  Algorithm                 Space Complexity
  ------------------------- ------------------
  Deterministic Selection   O(log n)
  Randomized Quickselect    O(log n) average

The recursive depth is proportional to the height of the recursion tree.

The deterministic algorithm introduces additional overhead due to: -
computing medians of groups - recursive median calculations

The randomized algorithm has lower constant overhead and therefore tends
to perform faster in practice.

------------------------------------------------------------------------

## Empirical Analysis

To evaluate the practical performance of both algorithms, benchmark
tests were conducted on different input distributions:

-   random
-   sorted
-   reverse‑sorted
-   duplicate‑heavy

Each test selected the median element of the array. The runtime was
measured over five trials, and the median runtime in milliseconds was
recorded.

Input sizes tested:

100, 500, 1000, 3000, 5000

### Benchmark Results

  Distribution     n      Deterministic (ms)   Randomized (ms)
  ---------------- ------ -------------------- -----------------
  random           100    0.067                0.035
  random           500    0.303                0.141
  random           1000   0.669                0.217
  random           3000   2.138                0.834
  random           5000   3.701                0.704
  sorted           100    0.045                0.018
  sorted           500    0.232                0.083
  sorted           1000   1.129                0.117
  sorted           3000   0.863                0.282
  sorted           5000   2.516                1.025
  reverse_sorted   100    0.065                0.035
  reverse_sorted   500    0.315                0.103
  reverse_sorted   1000   0.607                0.247
  reverse_sorted   3000   1.383                0.471
  reverse_sorted   5000   2.537                0.488
  duplicates       100    0.026                0.013
  duplicates       500    0.079                0.048
  duplicates       1000   0.175                0.190
  duplicates       3000   1.242                0.521
  duplicates       5000   2.435                0.855

------------------------------------------------------------------------

## Discussion of Results

The experimental results show that the randomized Quickselect algorithm
consistently performs faster than the deterministic Median of Medians
algorithm for most input sizes and distributions.

The deterministic algorithm performs additional work when selecting the
pivot, which increases constant overhead. While this guarantees
worst‑case linear time, it makes the algorithm slower in practice.

Randomized Quickselect benefits from a simpler pivot selection strategy.
By choosing pivots randomly, it avoids the cost of computing medians and
typically produces balanced partitions.

Even for sorted and reverse‑sorted inputs, randomized Quickselect
maintained strong performance. Random pivot selection prevents
consistently poor partitioning that would occur with fixed pivot
strategies.

Duplicate-heavy datasets were also handled correctly by both algorithms.
The partitioning logic successfully grouped equal elements together,
ensuring correctness and stable performance.

Overall, both algorithms scaled approximately linearly with increasing
input sizes, which aligns with the theoretical time complexity analysis.

------------------------------------------------------------------------

## Conclusion

This project implemented deterministic and randomized algorithms for
solving the selection problem. The deterministic Median of Medians
algorithm guarantees O(n) worst‑case time complexity, making it useful
for applications that require strict performance guarantees.

Randomized Quickselect achieves O(n) expected time complexity and
demonstrated significantly better practical performance during the
experiments.

The empirical results confirm the theoretical trade‑off:

-   Deterministic selection offers stronger theoretical guarantees.
-   Randomized selection offers better practical performance.

In real-world applications where worst‑case guarantees are not critical,
randomized Quickselect is typically the preferred solution due to its
simplicity and speed.


# PART-2: Arrays, Stacks, Queues, and Linked Lists

## 1. Introduction
In this assignment, I implemented four core data structures: arrays, stacks, queues, and singly linked lists. I also included an optional rooted tree structure to show how linked references can represent parent-child relationships. The goal of this work was not only to write the code, but also to understand how each structure behaves in terms of time complexity, memory use, and real-world practicality.

## 2. Implementation Overview
The array portion of the assignment was implemented using a Python list to simulate a dynamic array. The stack and queue were implemented in two ways: one using arrays and one using linked nodes. The linked list was implemented as a singly linked list with insertion, deletion, and traversal methods. For the optional extension, I created a rooted tree where each node stores its children and supports preorder traversal.

## 3. Step-by-Step Design Choices
### Arrays
I used a class called `DynamicArray` with methods for insert, delete, access, and traverse. This keeps the implementation simple and easy to test.

### Stacks
I used the Last-In-First-Out rule.  
- In the array version, `append()` acts as push and `pop()` removes the last item.
- In the linked-list version, each new node becomes the top.

### Queues
I used the First-In-First-Out rule.  
- In the array version, `append()` adds items, and `pop(0)` removes from the front.
- In the linked-list version, I maintained both front and rear pointers, which makes enqueue and dequeue more efficient.

### Singly Linked List
The linked list supports:
- insertion at the beginning
- insertion at the end
- insertion after a specific value
- deletion by value
- traversal through all nodes

### Optional Rooted Tree
The rooted tree contains a parent node and child references. I used preorder traversal to display the structure from root to leaves.

## 4. Time Complexity Analysis

| Data Structure | Operation | Time Complexity |
|---|---|---|
| Array | Access by index | O(1) |
| Array | Insert at end | O(1) amortized |
| Array | Insert at middle/front | O(n) |
| Array | Delete at middle/front | O(n) |
| Stack (array) | Push | O(1) |
| Stack (array) | Pop | O(1) |
| Queue (array) | Enqueue | O(1) |
| Queue (array) | Dequeue from front | O(n) |
| Stack (linked list) | Push | O(1) |
| Stack (linked list) | Pop | O(1) |
| Queue (linked list) | Enqueue | O(1) |
| Queue (linked list) | Dequeue | O(1) |
| Singly linked list | Insert at beginning | O(1) |
| Singly linked list | Insert at end | O(n) |
| Singly linked list | Delete by value | O(n) |
| Singly linked list | Traverse | O(n) |
| Rooted tree | Preorder traversal | O(n) |

## 5. Arrays vs Linked Lists for Stacks and Queues
For stacks, both arrays and linked lists work well. Arrays are easier to implement and usually perform very efficiently because elements are stored contiguously in memory. Linked-list stacks are also efficient for push and pop, but they use extra memory for node references.

For queues, the difference is more noticeable. An array-based queue becomes inefficient when removing elements from the front because all remaining elements shift left. A linked-list queue avoids this problem when front and rear pointers are maintained. Because of that, linked lists are often preferred when queue operations happen frequently.

## 6. Trade-Offs and Scenario-Based Comparison
Arrays are preferred when direct indexing is important, such as storing marks, monthly sales values, or sensor readings. They are simple and memory-efficient when the number of elements does not change too often.

Linked lists are better when the structure changes dynamically and frequent insertion or deletion is expected. For example, a task list that keeps changing or a playlist where songs are inserted and removed often can be modeled well with linked lists.

Stacks are useful when the latest item must be processed first. Typical examples include undo functionality in text editors, browser history navigation, or expression evaluation.

Queues are useful when requests must be processed in arrival order. Examples include print queues, CPU scheduling, customer service systems, and message buffering.

Rooted trees are useful for hierarchical relationships such as file systems, organization charts, menu structures, and XML or HTML documents.

## 7. Practical Applications
These data structures are used in many real-world systems:
- **Arrays:** image pixels, score tables, static datasets, lookup collections
- **Stacks:** undo/redo systems, function call stacks, bracket matching
- **Queues:** ticketing systems, networking buffers, printer spooling
- **Linked Lists:** dynamic memory structures, music playlists, graph adjacency representations
- **Rooted Trees:** folders, DOM trees, company hierarchies

## 8. Conclusion
This assignment helped me understand that choosing a data structure is not just about whether the code works. It is about choosing the structure that matches the workload. Arrays are strong when fast indexed access is needed. Linked lists are more flexible when updates happen often. Stacks and queues are simple but extremely useful abstractions that appear in many real applications. Overall, the implementation showed how performance, memory usage, and ease of implementation all influence design decisions.


