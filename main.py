from __future__ import annotations
from dataclasses import dataclass, field

class Node:
    value: int
    _next: Node = None
    
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
