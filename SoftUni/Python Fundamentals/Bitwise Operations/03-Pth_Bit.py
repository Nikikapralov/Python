number = int(input())
position = int(input())
shifted = number >> position
print(shifted & 1)
