'''
Linked List

Types of Linked List:-
1) Singly Linked List
2) Singly Circular List
3) Doubly Linked List
4) Doubly circular linked list

How linked list work:-

1)Define Node 
- data
- next

2)Create Linked List (head )----->none

'''

class Node:
    # class to create a new node
    def __init__(self, data):
        self.data = data
        self.next = None
Node1 = Node(10)
Node2 = Node(20)
Node1.next = Node2

print(f"Node1 data: {Node1.data}")
print(f"Node1.next data: {Node1.next.data}")
print(f"Node2 data: {Node2.data}")
print(f"Node2.next: {Node2.next}")

'''
Explaination:-
- This class represent single node in Linked List
- __init__(self, data) is a constructor
    - self.data : store the values of node
    - self.next : points to the next node in the list(initally set to None)
- Each node hold two piece of information

'''
class linkedList:
    #class for linked list
    def __init__(self):
        self.head = None
'''
Explanation :-
- This class represents the entire Linked List
- __init__(self) initize:
    - self.head : Points to the first node in the list(initially none)

'''
L1 = linkedList()
L1.head = Node(10) # manually add value 10

print(f"LinkedList head data: {L1.head.data}")
print(f"LinkedList head next: {L1.head.next}")

'''
Summary :-

Node Class : creates indiavidual nodes, storing data and reference

Dynamic Memory Allocation VS Deallocation Summary:-

Allocation ->
Happens automatically. When creates objects (Node(), list(), etc)

Deallocation:
Python garbage collector automatically frees memory when an object has no references
'''

