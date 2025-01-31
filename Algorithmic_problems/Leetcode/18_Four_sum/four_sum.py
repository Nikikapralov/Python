def four_sum(nums: list[int], target: int) -> list[int]:
    """
    TWO POINTER SOLUTION + SLIDING WINDOW

    Basically 3Sum but with 4 numbers.

    :param nums: An array of numbers.
    :param target: The target that the 4 numbers should sum up to.
    :return: List of combinations.
    """

    nums.sort()
    print(nums)
    result: list[list[int]] = []

    for index, first_number in enumerate(nums):

        # Do the check only after the first iteration and continue if the second number is the same as the first.
        if index >= 1 and first_number == nums[index - 1]:
            continue

        for i in range(index + 1, len(nums)):

            second_number: int = nums[i]
            # Do the check only after the first iteration and continue if the second number is the same as the first.
            # How much the index moves here is decided by sliding window.
            if i >= index + 2 and second_number == nums[i - 1]:
                continue

            left_pointer: int = i + 1
            right_pointer: int = len(nums) - 1

            while left_pointer != right_pointer and left_pointer < len(nums) - 1 and right_pointer >= 0:
                left_value: int = nums[left_pointer]
                right_value: int = nums[right_pointer]
                summed: int = first_number + second_number + left_value + right_value

                if summed == target:
                    #Found one combination
                    result.append([first_number, second_number, left_value, right_value])

                    # Find all combinations due to sorted list.
                    # Make sure the left pointer stays in bounds.
                    # Make sure the 2 pointers don't cross.
                    
                    while nums[left_pointer] == left_value and left_pointer != right_pointer and left_pointer < len(nums) - 1:
                        left_pointer += 1

                elif summed < target:
                    left_pointer += 1

                else:
                    right_pointer -= 1
    return result



#print(four_sum([1,0,-1,0,-2,2], 0))
#print(four_sum([2,2,2,2,2], 8))
#print(four_sum([-2,-1,-1,1,1,2,2], 0))
print(four_sum([2,-4,-5,-2,-3,-5,0,4,-2], -14))