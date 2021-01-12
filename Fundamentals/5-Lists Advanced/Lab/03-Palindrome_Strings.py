def palindrome_strings():
    words = input().split()
    wanted_word = input()
    counter = 0
    global palindromes
    palindromes = []
    for item in words:
        is_it_a_palindrome(item=item)
    for item_2 in palindromes:
        if item_2 == wanted_word:
            counter += 1
    print(palindromes)
    print(f'Found palindrome {counter} times')


def is_it_a_palindrome(item):
    if item == item[::-1]:
        palindromes.append(item)

palindrome_strings()
