for i in range(0, len(array)):
    for j in range(i + 1, len(array)):
        print(array[i] + "," + array[j])


"""This is O(N^2) although the second array gets progressively smaller, worst case is still very close to O(N^2)"""