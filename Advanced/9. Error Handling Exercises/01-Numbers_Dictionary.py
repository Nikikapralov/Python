numbers_dictionary = {}
try:
    line = input()

    while line != "Search":
        number_as_string = line
        number = int(input())
        numbers_dictionary[number_as_string] = number
        line = input()

    line = input()

    while line != "Remove":
        searched = line
        print(numbers_dictionary[searched])
        line = input()

    line = input()

    while line != "End":
        searched = line
        del numbers_dictionary[searched]
        line = input()

except ValueError:
    print('The variable number must be an integer')
except KeyError:
    print(f'Number does not exist in dictionary')
print(numbers_dictionary)

'''Not the best way to handle exceptions, but I was asked to use only 1 (try:)
   statement and multiple (except:) statements.'''
