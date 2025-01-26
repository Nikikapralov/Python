def three_sum(nums: list[int]) -> list[list[int]]:
    """
    TWO POINTER SOLUTION
    Given an integer array nums, return all the triplets
    [nums[i], nums[j], nums[k]] such that i != j, i != k,
    and j != k, and nums[i] + nums[j] + nums[k] == 0.

    Notice that the solution set must not contain duplicate triplets.

    SOLUTION:
    We set the first number as fixed and apply the two sum solution to the
    problem. We order the array to make accounting for duplicates easier since
    with the hash map solution we would have to order the array or write a custom
    hash function anyway.

    To get all unique combinations we make use of the sorted array.
    [-4, -1, -1, -1, 0, 1, 2, 2] for example.
    We start at -4. We find combinations.
    We start at -1. We find first combination. -1 -1 2
    We don't break the loop but we continue to find all combinations.
    How? Well the second number was already -1. If we choose -1 again, we end up with 2.
    So we need to move the pointer all the way to a new number: 0. We have -1 0 1
    We then move to 1, to 2 till the end.
    We then encounter -1 for our first number again (2 more times) but we say: Hey, I already have
    all of the combinations, I don't need them again so we skip.
    """

    nums.sort()
    result: list[list[int]] = []

    for index, first_number in enumerate(nums):

        # We add all pairs once and then never do it again.
        if index > 0 and first_number == nums[index - 1]:
            continue

        left_pointer: int = index + 1
        right_pointer: int = len(nums) - 1
        target: int = -first_number

        while left_pointer != right_pointer and left_pointer < len(nums):

            left_value: int = nums[left_pointer]

            right_value: int = nums[right_pointer]
            summed: int = left_value + right_value

            if summed == target:
                # Great, we found a pair.
                result.append([first_number, left_value, right_value])
                # We continue searching for pairs.
                left_pointer += 1
                # We continue moving the left pointer until we no longer have second vales that repeat.
                # Logic is, if the first value is the same and the second value is the same, then obviously
                # the third value will be the same again. So we move either the left or the right pointer
                # until that is no longer the case. We then check for the sum and either continue searching
                # for new, original combinations or we conclude that no more can be found.
                while nums[left_pointer] == left_value and left_pointer != right_pointer:
                    left_pointer += 1

                continue

            if summed < target:
                left_pointer += 1
            elif summed > target:
                right_pointer -= 1

    return result

print(three_sum([-1,0,1,2,2,-1, -1,-4]))
print(three_sum([0,0,0,0]))



