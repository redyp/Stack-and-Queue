from __future__ import annotations
from dataclasses import dataclass, field

@dataclass
class Node:
    value: int
    _next: Node = None

@dataclass
class Stack:
    value: int = field(repr=False)
    head: Node = field(init=False)
    lenght: int = field(init=False)
    
    def __post_init__(self):
        new_node = Node(self.value)
        self.head = new_node
        self.lenght = 1
        
    def __str__(self) -> str:
        if self.head is None:
            return "Stack Kosong"
        temp = self.head
        temp_str = ""
        while temp:
            temp_str += f"{temp.value} -> "
            temp = temp._next
        temp_str += "None"
        return temp_str
    
    def push(self, value: int):
        push_node = Node(value)
        if self.head is None:
            self.head = push_node
        else:
            push_node._next = self.head
            self.head = push_node
        self.lenght += 1
        return True
    
    def pop(self) -> Node:
        if self.lenght == 0:
            return None
        temp = self.head
        self.head = temp._next
        temp._next = None
        self.lenght -= 1
        return temp

@dataclass
class Queue:
    value: int = field(repr=False)
    head: Node = field(init=False)
    tail: Node = field(init=False)
    lenght: int = field(init=False)
    
    def __post_init__(self):
        new_node = Node(self.value)
        self.head = new_node
        self.tail = new_node
        self.lenght = 1
        
    def __str__(self) -> str:
        if self.head is None:
            return "Queue Kosong"
        temp = self.head
        temp_str = ""
        while temp:
            temp_str += f"{temp.value } -> "
            temp = temp._next
        temp_str += "None"
        return temp_str
    
    def enqueue(self, value: int):
        enqueue_node = Node(value)
        if self.head is None:
            self.head = enqueue_node
            self.tail = enqueue_node
        else:
            self.tail._next = enqueue_node
            self.tail = enqueue_node
        self.lenght += 1
        return True
    
    def dequeue(self) -> Node:
        if self.lenght == 0:
            return None
        temp = self.head
        if self.lenght == 1:
            self.head = None
            self.tail = None
        else:
            self.head = temp._next
            temp._next = None
        self.lenght -= 1
        return temp