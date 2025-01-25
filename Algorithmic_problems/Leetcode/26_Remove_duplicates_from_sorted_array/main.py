def remove_duplicates_from_sorted_array(nums: list[int]) -> list[int]:
    """
    Given an integer array nums sorted in non-decreasing order,
    remove the duplicates in-place such that each unique element
    appears only once. The relative order of the elements
    should be kept the same. Then return the number of unique elements in nums.

    Consider the number of unique elements of nums to be k,
    to get accepted, you need to do the following things:

    Change the array nums such that the first k elements of nums contain
    the unique elements in the order they were present in nums initially.
    The remaining elements of nums are not important as well as the size of nums.

    Return k.

    Solution:
    We loop through the array:
        if current == previous.
            we set the next item pointer to current.
        we do this until the array ends and we keep track of how many unique items we have.
        We subsequently return them.

    :param nums: A list of numbers that will be sorted and have to be filtered of duplicates IN PLACE.
    :return: The amount of unique elements.
    """
    last_unique_n_index: int = 0
    unique_items_count: int = 1

    for index, value in enumerate(nums):
        if value != nums[last_unique_n_index]:
            unique_items_count += 1
            last_unique_n_index += 1
            nums[last_unique_n_index] = value

    return unique_items_count

print(remove_duplicates_from_sorted_array([0,0,1,1,1,2,2,3,3,4]))



















