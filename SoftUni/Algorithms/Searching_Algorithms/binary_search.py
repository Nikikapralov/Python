"""
Binary search is an efficient searching algorithm.
It has a complexity of O(log N) and requires a sorted array.
It works in the following way:
    Find middle element.
    If not element we searched for, decide if smaller or higher.
    Get corresponding half of the array.
    Repeat until element found.

This algorithm is a good candidate for a recursive implementation, although it must be noted
that a while loop implementation is more beneficial since we won't be using the memory from the
stack and won't be limited by it. The while loop implementation is quite easy to code, but I want
to have some fun and will provide the recursive approach since I enjoy recursion.
"""
from typing import Any


def binary_search(entries: list[Any], searched_for: Any) -> bool:
    """
    Implement binary search.
    @param entries: A list of entries to search from.
    @param searched_for: Value that we are searching for.
    @return: True/False.
    """
    # If list is empty, return not found.
    if not entries:
        return False

    middle_index: int = len(entries) // 2
    potential_value: Any = entries[middle_index]

    # If the middle value is our value, return found.
    if potential_value == searched_for:
        return True

    # Go left.
    if searched_for < potential_value:
        new_entries: list[Any] = entries[:middle_index]
    else:
        # Go right.
        new_entries: list[Any] = entries[middle_index + 1:]

    # Keep going until we either find it or the list is empty.
    return binary_search(entries=new_entries, searched_for=searched_for)


values: list[int] = [n for n in range(3)]
print(binary_search(entries=values, searched_for=1))
