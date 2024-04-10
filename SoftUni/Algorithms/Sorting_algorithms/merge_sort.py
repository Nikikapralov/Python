"""
Merge sort is a very efficient sorting algorithm, working best when we have some of the
elements already sorted. Even when not, this algorithm is much better than the ones we have
learned up to this point, except for maybe Bucket sort. It uses the divide and conquer methodology.

Complexity - O(N log N)
In place - No, requires the creation of multiple smaller arrays that add up to O(N)

How merge sort works:
Get the unsorted array and divide it in half.
For each such array, keep dividing until the array cannot be divided anymore.
At this point, merge the last 2 lists and order them, repeating this going up the chain.

Why is this O(N log N)?
When we divide the elements and merge them together, we must at most do N passes through all elements.
Since we have divided them and merged before, some of them will already be ordered. This results in a O(N log N)
complexity.
"""

unsorted_list: list[int] = [3, 8, 9, 7, 1, 2, 3, 4, 5]


def merge_sort(unsorted_list: list[int]) -> list[int]:
    """
    Get the unsorted array and divide it in half.
    For each such array, keep dividing until the array cannot be divided anymore.
    At this point, merge the last 2 lists and order them, repeating this going up the chain.
    @param unsorted_list: The unsorted list that we have to sort.
    @return: A list of sorted items.
    """
    # If it cannot be divided further, return.
    if len(unsorted_list) == 1:
        return unsorted_list

    middle_index: int = (len(unsorted_list) - 1) // 2 + 1
    left: list[int] = unsorted_list[:middle_index]
    right: left[int] = unsorted_list[middle_index:]
    # Branch left
    sorted_left: list[int] = merge_sort(unsorted_list=left)
    # Branch right
    sorted_right: list[int] = merge_sort(unsorted_list=right)

    sorted_result: list[int] = []

    left_iteration: int = 0
    right_iteration: int = 0

    # Until the array lengths are equal, keep comparing left with right and filling the new array.
    while left_iteration < len(sorted_left) and right_iteration < len(sorted_right):
        first_element: int = sorted_left[left_iteration]
        second_element: int = sorted_right[right_iteration]

        if first_element >= second_element:
            sorted_result.append(second_element)
            right_iteration += 1
        else:
            sorted_result.append(first_element)
            left_iteration += 1

    # Put all the rest of the left array
    while left_iteration < len(sorted_left):
        sorted_result.append(sorted_left[left_iteration])
        left_iteration += 1

    # Put all the rest of the right array
    while right_iteration < len(sorted_right):
        sorted_result.append(sorted_right[right_iteration])
        right_iteration += 1

    """
    3, 8, 9 
    3 8, 9
    3, 8 
    3 8
    3 8, 9
    3 8 9
    
    After the split
    Compare 3 and 8, put 3 first, exit first loop, put all from right inside (8).
    3 8, 9 - Compare 3 and 9, put 3 inside. Compare 8 and 9, put 8 inside. Put all from second list inside.
    3 8 9.
    Return
    
    Overall a very smart algorithm. GG.
    """

    return sorted_result

print(unsorted_list)
print(merge_sort(unsorted_list=unsorted_list))
