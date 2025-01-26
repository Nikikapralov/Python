def container_with_most_water(height: list[int]) -> int:
    """
    TWO POINTER SOLUTION
    You are given an integer array height of length n.
    There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
    Find two lines that together with the x-axis form a container, such that the container contains the most water.
    Return the maximum amount of water a container can store.

    Solution:
    Area = a * b
    I set a pointer to the right and to the left of the array.
    I calculate the area between the 2 columns.
    I move the smaller pointer one position.
    I calculate the area again.
    Repeat until the biggest area is found.

    This works because with this approach, we are limited by the height of the smallest wall. (Water overflow)
    and we subsequently squeeze the container tighter and tighter until we reach out of options.

    For each column:

    :param height: An array of columns, where each integer value is the height of the column.
    :return: The maximum area of the water the container can hold.
    """
    area: int = 0
    right_pointer: int = len(height) - 1
    left_pointer: int = 0

    while right_pointer != left_pointer:
        right: int = height[right_pointer]
        left: int = height[left_pointer]
        distance: int = right_pointer - left_pointer

        if right > left:
            smallest = left
            left_pointer += 1
        else:
            smallest = right
            right_pointer -= 1

        new_area = distance * smallest

        if new_area > area:
            area = new_area

    return area








print(container_with_most_water(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(container_with_most_water(height=[1, 1]))
