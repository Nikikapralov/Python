words = ['i', 'am', 'learning', 'recursion']

def capitalizeWords(arr, index=0):
    if index == len(arr):
        return arr
    arr[index] = arr[index].upper()
    return capitalizeWords(arr, index + 1)

print(capitalizeWords(words))
