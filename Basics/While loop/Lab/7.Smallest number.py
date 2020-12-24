import sys
lowest_number = sys.maxsize
command = input()
while command != 'Stop':
    command = int(command)
    if command < lowest_number:
        lowest_number = command
    command = input()
print(lowest_number)