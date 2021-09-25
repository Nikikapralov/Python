def reverse(array):
    for i in range(0,int(len(array)/2)):
        other = len(array)-i-1
        temp = array[i]
        array[i] = array[other]
        array[other] = temp
    print(array)

reverse(arrayA)

"""This will be complexity of O(N/2) since we only loop around half of the array."""