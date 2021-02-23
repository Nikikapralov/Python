import sys
highest_number = -sys.maxsize
command = input()
while command != 'Stop':
    command = int(command)
    if command > highest_number:
        highest_number = command
    command = input()
print(highest_number)