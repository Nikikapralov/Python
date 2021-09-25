for i in range(len(arrayA)):
    for j in range(len(arrayB)):
        if arrayA[i] < arrayB[j]:
            print(str(arrayA[i]) + "," + str(arrayB[j]))

"""So this is going to be O(AB)"""