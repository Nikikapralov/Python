"""
Quick sort is one of the fastest sorting algorithms. It is a divide and conquer algorithm that
can be easily implemented with recursion. Unlike merge sort, it is unstable.

Complexity: O (N log N)
In place: Yes.
Stable: No, this is an unstable algorithm.

How quicksort works:
Choose the first element of the array as a pivot.
Loop through all rest elements and compare them.
If smaller, do nothing.
If greater - mark as swap.
Next time you find a smaller, swap smaller with the greater and
continue for all items.
At the end, swap pivot with the last swap number.

Now split the list into two and continue doing it until you have just 1 pivot number,
meaning the ending_index not > starting index.

Very good in sorting arrays since we need random access due to inplace nature of the algorithm. (index needed)
Very efficient for small datasets.
Choosing the pivot is very important. We need to choose the pivot in such a way, so that the lists are split
equally. Otherwise we may get a complexity of O(N**2). Works well on evenly distributed elements, like bucket sort.

How to choose the pivot element? Use the median of 3 method, picking the first, last and middle elements, then getting
the median of those elements as the pivot. That should work sufficiently well for quicksort.

P.S. @*@#&%@ this algorithm.
"""

unsorted_list: list[int] = [0, 1, 7, 8, 2, 9, 3, 5, 4, 6]
test: list[int] = [3, 2, 5, 0, 1, 4, 7, 6, 9, 8]


def quicksort(unsorted_list: list[int], start_index: int = 0, ending_index: int | None = None) -> None:
    """
    Choose the middle element of the array as a pivot.
    Loop through all rest elements and compare them.
    If bigger, do nothing.
    If smaller or equal, swap += 1 (If swap is none, set swap to 0)
        if swap > index -> swap

    Now split the list into two and continue doing it until you have just 1 pivot number,
    meaning the ending_index not > starting index.
    @param unsorted_list: The list that we have to sort.
    @param start_index: The start index for the loop.
    @param ending_index: The end index for the loop.
    @return: None as the sorting is done in place.
    """

    if ending_index is None:
        ending_index: int = len(unsorted_list)

    if start_index >= ending_index:
        return

    pivot_index: int = ending_index - 1
    pivot_element: int = unsorted_list[pivot_index]


    # # swap with last item
    # unsorted_list[pivot_index], unsorted_list[ending_index - 1] = unsorted_list[ending_index - 1], unsorted_list[pivot_index]
    swap_index: int | None = None

    for index in range(ending_index):
        element: int = unsorted_list[index]

        if element <= pivot_element:
            if swap_index is not None:
                swap_index += 1
            else:
                swap_index = 0

            if unsorted_list[swap_index] > element:
                unsorted_list[swap_index], unsorted_list[index] = unsorted_list[index], unsorted_list[swap_index]

    # Branch left
    quicksort(unsorted_list=unsorted_list, start_index=0, ending_index=swap_index)
    # Branch right
    quicksort(unsorted_list=unsorted_list, start_index=swap_index + 1, ending_index=ending_index)

print(test)
quicksort(unsorted_list=test)
print(test)
