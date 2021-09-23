def product_of_an_array(array):
    if not array:
        return 1
    return array.pop() * product_of_an_array(array)

print(product_of_an_array([1, 2, 3, 4]))