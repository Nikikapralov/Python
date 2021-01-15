list_of_numbers = input().split()
results = {}
for number in list_of_numbers:
    amount = list_of_numbers.count(number)
    if number in results:
        continue
    else:
        results[number] = amount
for key, value in results.items():
    print(f'{float(key):.1f} - {value} times')