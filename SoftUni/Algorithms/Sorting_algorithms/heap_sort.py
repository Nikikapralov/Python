"""
Heap sort is a very efficient sorting algorithm that uses a heap to sort the items.

Complexity: O(N logN)
In place: Yes and No, depending on implementation. This one currently is not in place.
Stable: Not a stable algorithm.

How heap sort works?
Add all items to the heap or transform the array into a heap.
Start popping items from the heap and adding them to the new list.
Alternatively, for each element in the heap, perform the heapify function to rearrange them in order.

"""
from Trees.python_list_trees.heap import MinHeap


def heap_sort(unsorted_list: list[int]) -> list[int]:
    """
    Add all elements to the heap then start popping them one by one and adding to a new list.
    Lazy not in place implementation because I don't want to export the heapify function only
    and just want to use the MinHeap structure we already have.
    @param unsorted_list: The list to sort.
    @return: The list that is sorted.
    """
    result: list[int] = []
    min_heap: MinHeap = MinHeap(size=len(unsorted_list))
    [min_heap.insert(priority=element) for element in unsorted_list]
    [result.append(min_heap.extract()) for _ in min_heap]
    return result

unsorted_list: list[int] = [3, 4, 1, 6, 7, 9]
print(heap_sort(unsorted_list=unsorted_list))