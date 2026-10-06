from __future__ import annotations
from dataclasses import dataclass


# 1. RÄCKA - elementen ligger bredvid varandra i minnet
"""
[Anna] [Erik] [Sara]
Index: O(1)   Sök: O(n)   Sätt in/ta bort: O(n)
"""
rakka = ["Anna", "Erik", "Sara"]
print(rakka[1])                 # Erik


# 2. LÄNKAD LISTA - varje nod pekar på nästa
"""
Anna -> Erik -> Sara -> None
Sök: O(n)   Sätt in/ta bort: O(1)
"""
@dataclass
class Node:
    data: str
    next: Node | None = None

head = Node("Anna", Node("Erik", Node("Sara")))
print(head.next.data)           # Erik


# 3. DUBBELLÄNKAD LISTA - pekar framåt OCH bakåt
"""
None <- Anna <-> Erik <-> Sara -> None
Som länkad lista, men kan gå bakåt. Mer minne.
"""
@dataclass
class DNode:
    data: str
    next: DNode | None = None
    prev: DNode | None = None

anna, erik = DNode("Anna"), DNode("Erik")
anna.next = erik
erik.prev = anna
print(erik.prev.data)           # Anna


# 4. SKIPLIST - sorterad lista med genvägar
"""
Nivå 1:  Anna ---------> Sara       (genväg)
Nivå 0:  Anna -> Erik -> Sara       (alla)
Sök: O(log n) i snitt, O(n) i värsta fall
"""
@dataclass
class SkipNode:
    data: str
    next: list                  # en pekare per nivå

sara_s = SkipNode("Sara", [None, None])
erik_s = SkipNode("Erik", [sara_s])
anna_s = SkipNode("Anna", [erik_s, sara_s])   # next[0]=Erik, next[1]=genväg till Sara
print(anna_s.next[1].data)      # Sara, hoppade över Erik


# STACK = LIFO (sist in, först ut)
stack = []
stack.append("A")    # push  O(1)
stack.append("B")    # push  O(1)
print(stack.pop())   # pop   O(1)  -> B

# KÖ = FIFO (först in, först ut)
from collections import deque
queue = deque()
queue.append("A")        # enqueue  O(1)
queue.append("B")        # enqueue  O(1)
print(queue.popleft())   # dequeue  O(1)  -> A
