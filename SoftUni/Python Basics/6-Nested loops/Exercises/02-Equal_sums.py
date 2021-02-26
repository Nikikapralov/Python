number1 = int(input())
number2 = int(input())
for number in range(number1, number2 + 1):
    number_to_str = str(number)
    odd_sum = 0
    even_sum = 0
    for index, digit in enumerate(number_to_str):
        current_digit = int(digit)
        current_index = int(index)
        if current_index % 2 == 0:
            even_sum += current_digit
        else:
            odd_sum += current_digit
    if odd_sum == even_sum:
        print(number, end=" ")