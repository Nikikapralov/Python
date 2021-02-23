command = input()
coffee_count = 0
while command != 'END':
    if command.islower():
        if command == 'coding' or command == 'cat' or command == 'dog' or command == 'movie':
            coffee_count += 1

    elif command.isupper():
        if command == 'CODING' or command == 'CAT' or command == 'DOG' or command == 'MOVIE':
            coffee_count += 2
    command = input()
if coffee_count > 5:
    print(f'You need extra sleep')
else:
    print(coffee_count)
