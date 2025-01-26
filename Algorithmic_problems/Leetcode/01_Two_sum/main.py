def two_sum(nums: list[int], target: int) -> list[int]:
    """
    HASHMAP SOLUTION
    Given an array of integers nums and an integer target,
    return indices of the two numbers such that they add up to target.

    My solution:
    For each number in numbers: O(N)
        Find 9 - number and save it in map with index. (O1)
        If number in map: (O1)
            return current_index and number_index. (O1)

    :param nums: The input array.
    :param target: The number to sum up to.
    :return: A list with the indexes of the two numbers that sum up to the target.
    """
    number_index_map: dict[int, int] = {}

    for index, value in enumerate(nums):
        number: int = target - value
        if number in number_index_map:
            result: list[int] = [number_index_map[number], index]
            return result
        number_index_map[value] = index


print(two_sum(nums=[2, 7, 11, 15], target=9))
print(two_sum(nums=[3, 2, 4], target=6))
print(two_sum(nums=[3, 3], target=6))
