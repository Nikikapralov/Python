from __future__ import annotations
from typing import Any
from abc import ABC, abstractmethod

"""
The binary heap is a tree datastructure.
Properties of a heap:
- A complete binary tree, where only the last level is left unfilled. 
- Min heap (where the lowest element is the root)
- Max heap (where the highest element is the root)
- Used for priority queues (removal of root element takes only O(1) time)

The python list or array implementation is the correct one for a binary heap.
"""


class Heap(ABC):
    """
    A python list heap implementation.
    """
    @abstractmethod
    def __init__(self, size: int):
        self._size: int = size + 1
        self.heap_items: list[Any | None] = [None] * self._size
        self.current_size: int = 0

    @property
    def heap_items(self):
        return self._heap_items[1::]

    @heap_items.setter
    def heap_items(self, value):
        self._heap_items = value

    def peek(self) -> Any:
        """
        Return the root node.
        """
        return self.heap_items[0]

    @abstractmethod
    def _heapify_insert(self, index: int, priority: int) -> None:
        """
        Reorder the heap based on Min or Max property for insertion.
        """
        pass

    @abstractmethod
    def _heapify_extract(self, index: int, priority: int) -> None:
        """
        Reorder the heap based on Min or Max property for extraction.
        """
        pass

    def insert(self, priority: int) -> Heap:
        """
        Insert a node. Check if the node is higher or lower than the min heap and reorder the
        tree accordingly. The heap is not a Binary Search tree and as such only the root element is
        important.
        @param priority: The priority value of the node.
        """
        new_index: int = self.current_size + 1
        if new_index > self._size:
            print("Heap full. Cannot insert.")
            return self
        self.current_size += 1
        self._heap_items[new_index] = priority

        self._heapify_insert(index=new_index, priority=priority)

        return self

    def extract(self) -> Heap:
        """
        Return the root node and appoint a new root node on the Heap.
        Replace the root node with the last element of the heap and
        then heapify the tree.
        """
        last_el_index: int = self.current_size
        last_node: Any = self._heap_items[last_el_index]
        self._heap_items[last_el_index], self._heap_items[1] = self._heap_items[1], self._heap_items[last_el_index]
        self._heap_items[last_el_index] = None
        self.current_size -= 1

        self._heapify_extract(index=1, priority=last_node)
        return self

    def delete_heap(self) -> Heap:
        """
        Resets the heap_items list to None for every slot in the gives by the user size.
        """
        self.heap_items: list[Any | None] = [None] * self._size
        return self

    def __iter__(self):
        for entry in self.heap_items[1::]:
            yield entry


class MinHeap(Heap):
    def __init__(self, size: int):
        super().__init__(size=size)

    def _heapify_insert(self, index: int, priority: int) -> None:
        """
        Reorder the heap tree for insertion.
        The algorithm bubbles from bottom to up.
        @param index: The index for the current node.
        @param priority: The priority value of the node.
        """
        parent_index: int = index // 2
        if parent_index < 1:
            return
        if self._heap_items[parent_index] <= priority:
            return

        self._heap_items[parent_index], self._heap_items[index] = (self._heap_items[index],
                                                                       self._heap_items[parent_index])
        self._heapify_insert(index=parent_index, priority=priority)

    def _heapify_extract(self, index: int, priority: int) -> None:
        """
        Not the clearest implementation but it works like that:
        Check if left child -> continue swapping left.
        Check if right child -> continue swapping right.
        Check if both children -> get smallest -> continue swapping smallest.
        The algorithm drills from top to bottom.
        @param index: Index of the current position of the node.
        @param priority: Priority of the current position of the node.
        @return: None.
        """
        left_child_index: int = index * 2
        right_child_index: int = index * 2 + 1
        # If bigger than the current size (list index out of range) return.
        if left_child_index >= self._size or right_child_index >= self._size:
            return
        left_child: tuple[Any, int] = self._heap_items[left_child_index], left_child_index
        right_child: tuple[Any, int] = self._heap_items[right_child_index], right_child_index

        # If both are none, we are done and have finished swapping.
        if left_child[0] is None and right_child[0] is None:
            return

        elif right_child[0] is None:
            if left_child[0] < priority:
                self._heap_items[index], self._heap_items[left_child[1]] = (self._heap_items[left_child[1]],
                                                                         self._heap_items[index])
                self._heapify_extract(index=left_child[1], priority=priority)
            return

        elif left_child[0] is None:
            if right_child[0] < priority:
                self._heap_items[index], self._heap_items[right_child[1]] = (self._heap_items[right_child[1]],
                                                                         self._heap_items[index])
                self._heapify_extract(index=right_child[1], priority=priority)
            return

        else:
            if left_child[0] >= priority and right_child[0] >= priority:
                return None

            if left_child[0] >= right_child[0]:
                smaller: tuple[Any, int] = right_child
            else:
                smaller: tuple[Any, int] = left_child

            self._heap_items[index], self._heap_items[smaller[1]] = (self._heap_items[smaller[1]],
                                                                     self._heap_items[index])

            self._heapify_extract(index=smaller[1], priority=priority)
            return None


h = MinHeap(10)
h.insert(1)
h.insert(7)
h.insert(3)
h.insert(9)
h.insert(2)
h.insert(5)
h.insert(4)

print(h.heap_items)
h.extract()
print(h.heap_items)






