"""
Sorting terminology:
In place - the array is modified and no extra space is required.
Out of place - extra space is required to do the sorting.
Stable - if two items are equal, they retain their original order.
Unstable - they do not retain their original order.

Increasing order - 1,2,3 - no duplicates
Decreasing order - 3,2,1 - no duplicates

Non increasing order - 3,2,2,1 - duplicates allowed
Non decreasing order - 1,2,2,3 - duplicates allowed

Bubble sort (sinking sort):

Start at the beginning and for each pair, check which entry is bigger and
swap them accordingly. Each run will bubble the highest element to the right
of the array. Subsequent runs exclude the sorted number. Repeat until the
array is sorted.

O(n**2) algorithm, in place. Can be coded to be stable and unstable.

Of course, you can write this sorting algorithm with 2 nested for loops and
save the memory from the stack but I really enjoy recursion so I write recursion.
"""
unsorted_list: list[int] = [2, 3, 1, 9, 2, 8, 7, 800]


def bubble_sort(list_to_sort: list[int], index=None) -> None:
    """
    Start at the beginning and for each pair, check which entry is bigger and
    swap them accordingly. Each run will bubble the highest element to the right
    of the array. Subsequent runs exclude the sorted number. Repeat until the
    array is sorted.
    @param list_to_sort: The list which is to be sorted.
    @param index: The index until which the sorting operation should be performed.
    Used in the recursive flow.
    @return: None as it modifies the list in place. Alternatively, can be made to return a
    new list, which will break the in place implementation and increase memory usage.
    """
    if index is None:
        index: int = len(list_to_sort) - 1

    # The array is sorted.
    if index == -1:
        return

    # Do the swapping operations.
    for ind in range(index):
        first: int = list_to_sort[ind]
        second: int = list_to_sort[ind + 1]

        if first > second:
            list_to_sort[ind], list_to_sort[ind + 1] = list_to_sort[ind + 1], list_to_sort[ind]

    # Recursively bubble all the values.
    bubble_sort(list_to_sort=list_to_sort, index=index-1)


bubble_sort(list_to_sort=unsorted_list)
print(unsorted_list)
