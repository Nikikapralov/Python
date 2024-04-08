"""
Selection sort, (also known as Nick sort - since I tried to come up with a sorting algorithm and
came up with that on my own) is a quite poor sorting algorithm.

Complexity - O(n**2).
In place - yes.
Stability - yes, a stable algorithm.

How selection sort works:
Find smallest element, swap with first element.
Find next smallest element, swap with second element.
Repeat until no more elements are found.

Can be written as 2 nested for loops which is what I will do for a change.
"""
import sys

unsorted_list: list[int] = []


def selection_sort(list_to_be_sorted: list[int]) -> None:
    """
    Find smallest element, swap with first element.
    Find next smallest element, swap with second element.
    Repeat until no more elements are found.
    @param list_to_be_sorted: The list that we want to sort.
    @return: None as the sorting is done in place.
    """
    highest_index: int = len(list_to_be_sorted)

    # For each sublist in the list.
    for i in range(highest_index):
        smallest_number: int = sys.maxsize
        smallest_number_index: int | None = None

        # Find the smallest number.
        for i_2 in range(i, highest_index):
            number: int = list_to_be_sorted[i_2]
            if number < smallest_number:
                smallest_number_index = i_2
                smallest_number = number

        # Replace it with the starting number of the sublist.
        if smallest_number_index is not None:
            list_to_be_sorted[smallest_number_index], list_to_be_sorted[i]\
                = list_to_be_sorted[i], list_to_be_sorted[smallest_number_index]

print(unsorted_list)
selection_sort(list_to_be_sorted=unsorted_list)
print(unsorted_list)
