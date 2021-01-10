def palindrome(number):
    for instance in number:
        list_instance = []
        reversed_instance = []
        for x in instance:
            list_instance.append(x)
        reversed_instance = list_instance[::-1]
        if list_instance == reversed_instance:
            print('True')
        else:
            print('False')



number = input().split(', ')
execute = palindrome(number)
