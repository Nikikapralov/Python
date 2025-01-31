def three_sum_closest(nums: list[int], target: int) -> int | None:
    """
    TWO POINTER SOLUTION
    Given an integer array nums of length n and an integer target,
    find three integers in nums such that the sum is closest to target.

    Return the sum of the three integers.

    Fix the first number.
    Start going through second and third with a 2 pointer solution, hoping to get to target.
    Find the sum and the difference of it to target.

    OPTIMISATION:
    Sort the array.
    If the array is sorted, we can notice when the difference starts getting bigger.
    At that point, we know that we have reached the most optimal sum.

    :param nums: A list of integers holding the data.
    :param target: The amount that we have to sum up to.
    :return:
    """
    import sys

    nums.sort()
    lowest_difference: int = sys.maxsize
    result: int | None = 0

    for index, first_number in enumerate(nums):

        # No need to compute repeated sums in an array since they give the same result anyway.

        if index >= 1 and first_number == nums[index - 1]:
            continue

        left_pointer: int = index + 1
        right_pointer: int = len(nums) - 1

        # Pointers don't cross and stay in bounds of array.
        while left_pointer != right_pointer and left_pointer < len(nums) and right_pointer >= 0:
            left_value: int = nums[left_pointer]
            right_value: int = nums[right_pointer]
            summed: int = first_number + left_value + right_value
            difference: int = abs(target - summed)

            if difference == 0:
                result = summed
                return result

            # Difference is bigger than lowest difference so we need to lower the sum.
            if difference < lowest_difference:
                lowest_difference = difference
                result = summed

            # Move pointers based on the sum comparison with the target.
            if summed < target:
                left_pointer += 1
            else:
                right_pointer -= 1

    return result

#print(three_sum_closest([-1,2,1,-4], 1))
#print(three_sum_closest([0, 0, 0], 1))
#print(three_sum_closest([1,1,1,0], -100))
#print(three_sum_closest([2, 5, 6, 7], 16))
print(three_sum_closest([4,0,5,-5,3,3,0,-4,-5], -2))


