#numbers = list(map(lambda number: int(number), input().split(', ')))
#even = []
#for index, value in enumerate(numbers):
   # if value % 2 == 0:
     #   even.append(index)
#print(even)


numbers = [int(number) for number in input().split(', ')]
even = [index for index in range(len(numbers)) if numbers[index] % 2 == 0]
print(even)