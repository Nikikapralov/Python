"""
Bucket sort is an algorithm that works well for uniformly distributed data.

Complexity - O(n + logN) when using quicksort with it.
In place - no, has a space complexity of O(N + K).

How bucket sort works:
First, create buckets where we separate the values.
Second, separate the values in the buckets according to their range.
Third, order each bucket on its own.
"""


import math

from Sorting_algorithms.insertion_sort import insertion_sort

unsorted_list: list[int] = [9, 2, 4, 6, 7, 1, 8, 5]


def bucket_sort(unordered_list: list[int]) -> list[int]:
    """
    First, create buckets where we separate the values.
    Second, separate the values in the buckets according to their range.
    Third, order each bucket on its own.

    The formulas work for bucket sort with negative numbers.

    @param unordered_list: List we have to order.
    @return: List with ordered values.
    """
    amount_of_buckets: int = round(math.sqrt(len(unordered_list)))
    min_value: int = min(unordered_list)
    max_value: int = max(unordered_list)
    range_value: float = (max_value - min_value) / amount_of_buckets

    buckets: list[list[int]] = [[] for _ in range(amount_of_buckets)]

    for element in unordered_list:
        if element == max_value:
            buckets[-1].append(element)
        else:
            bucket_index: int = math.floor((element - min_value) / range_value)
            buckets[bucket_index].append(element)


    sorted_array: list[int] = []

    for bucket in buckets:
        insertion_sort(bucket)
        sorted_array.extend(bucket)

    return sorted_array

print(unsorted_list)
print(bucket_sort(unordered_list=unsorted_list))