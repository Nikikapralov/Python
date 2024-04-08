"""
Insertion sort

Complexity - O(n**2)
In place - True
Stability - can be written to be stable or unstable

Insertion sort:
Get the first element. Put in on the sorted side.
Get the second element. Put it either left or right on
the sorted side. If it is not directly, keep moving the
elements until you find its spot.
Repeat for each element in the array.


Insertion sort is good to implement when we have a continuous inflow of numbers.
But if you think about it, we have a sorted sublist. Well in that case, why your the
linear mechanics and not do a binary search to find its position? Enter...Quicksort!
"""


def insertion_sort(unsorted_array: list[int]) -> None:
    """
    Get the first element. Put in on the sorted side.
    Get the second element. Put it either left or right on
    the sorted side. If it is not directly, keep moving the
    elements until you find its spot.
    Repeat for each element in the array.

    @param unsorted_array: The array that we have to sort.
    @return: None as the sorting is done in place.
    """
    highest_index: int = len(unsorted_array)
    # We skip the first element because we always place it there, nothing to compare with.
    for i in range(1, highest_index):
        element: int = unsorted_array[i]
        # We loop around from back to start
        for i_2 in range(i - 1, -2, -1):

            # If we reach here, that means that this is the smallest element we have encountered yet
            # and it is on the first position.

            if i_2 == -1:
                unsorted_array[0] = element
                break

            last_sorted_el: int = unsorted_array[i_2]

            # If current element is smaller, we copy and continue
            if element < last_sorted_el:
                unsorted_array[i_2 + 1] = last_sorted_el

            # Otherwise replace the position/copy and break
            else:
                unsorted_array[i_2 + 1] = element
                break
