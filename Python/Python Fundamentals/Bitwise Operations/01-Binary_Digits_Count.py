number = int(input())
digit = input()
binary_number = bin(number)
if digit == '0':
    result = binary_number.count(digit) - 1
else:
    result = binary_number.count(digit)
print(result)

