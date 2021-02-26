import sys
global array
array = input().split()
def exchange(array_index):
    global Flag_1
    Flag_1 = False
    index = 0
    exchange_list = []
    global flat_list
    flat_list = []
    array_command_list = array_command.split()
    array_command_list[1] = int(array_command_list[1])
    index = array_command_list[1]
    if array_command_list[1] > (len(array) - 1):
        print('Invalid index')
        Flag_1 = True
        return
    else:
        exchange_list.append(array[index + 1::])
        exchange_list.append(array[:index + 1:])
        for sublist in exchange_list:
            for item in sublist:
                flat_list.append(item)


def max_even_odd(max_even_odd_index):
    biggest = -sys.maxsize
    index_of_biggest = 1
    if 'odd' in array_command:
        for index, value in enumerate(array):
            value = int(value)
            if value % 2 == 1:
                if value >= biggest:
                    biggest = value
                    index_of_biggest = index
        if biggest == -sys.maxsize:
            print('No matches')
            return

    elif 'even' in array_command:
        for index, value in enumerate(array):
            value = int(value)
            if value % 2 == 0:
                if value >= biggest:
                    biggest = value
                    index_of_biggest = index
        if biggest == -sys.maxsize:
            print('No matches')
            return
    print(index_of_biggest)


def min_even_odd(min_even_odd_index):
    smallest = sys.maxsize
    index_of_smallest = None
    if 'odd' in array_command:
        for index, value in enumerate(array):
            value = int(value)
            if value % 2 == 1:
                if value < smallest:
                    smallest = value
                    index_of_smallest = index
        if smallest == sys.maxsize:
            print('No matches')
            return

    elif 'even' in array_command:
        for index, value in enumerate(array):
            value = int(value)
            if value % 2 == 0:
                if value < smallest:
                    smallest = value
                    index_of_smallest = index
        if smallest == sys.maxsize:
            print('No matches')
            return
    print(index_of_smallest)


def first_even_odd(first_batch_of_numbers):
    if 'even' in array_command:
        Flag = False
        list_of_first_even = []
        list_of_command = array_command.split()
        amount = list_of_command[1]
        amount = int(amount)
        if amount > len(array):
            print('Invalid count')
            return
        counter = 0
        while True:
            if Flag:
                break
            for index, value in enumerate(array):
                value = int(value)
                if counter == amount:
                    Flag = True
                    break
                if value % 2 == 0:
                    counter += 1
                    list_of_first_even.append(value)
            print(list_of_first_even)

    if 'odd' in array_command:
        Flag = False
        list_of_first_odd = []
        list_of_command = array_command.split()
        amount = list_of_command[1]
        amount = int(amount)
        if amount > len(array):
            print('Invalid count')
            return
        counter = 0
        while True:
            if Flag:
                break
            for index, value in enumerate(array):
                value = int(value)
                if counter == amount:
                    Flag = True
                    break
                if value % 2 == 1:
                    counter += 1
                    list_of_first_odd.append(value)
        print(list_of_first_odd)


def last_even_odd(last_batch_of_numbers):
    if 'even' in array_command:
        Flag = False
        counter = 0
        even_list = []
        list_of_command = array_command.split()
        amount = list_of_command[1]
        amount = int(amount)
        if amount > len(array):
            print('Invalid count')
            return
        array.reverse()
        for item in array:
            item = int(item)
            if amount == counter:
                break
            if item % 2 == 0:
                even_list.append(item)
                counter += 1
            array.reverse()
        print(even_list)




# reverse the list, iterate through it while checking if its even or odd, append in another list then reverse the array again to return to normal

    if 'odd' in array_command:
        counter = 0
        odd_list = []
        list_of_command = array_command.split()
        amount = list_of_command[1]
        amount = int(amount)
        if amount > len(array):
            print('Invalid count')
            return
        array.reverse()
        for item in array:
            item = int(item)
            if amount == counter:
                break
            if item % 2 == 1:
                odd_list.append(item)
                counter += 1
            array.reverse()
        print(odd_list)


while True:
    array_command = input()
    if array_command == 'end':
        break
    elif 'exchange' in array_command:
        exchange(array_command)
        if not Flag_1:
            array = flat_list
    elif 'max' in array_command:
        max_even_odd(array_command)
    elif 'min' in array_command:
        min_even_odd(array_command)
    elif 'first' in array_command:
        first_even_odd(array_command)
    elif 'last' in array_command:
        last_even_odd(array_command)

print(array)
