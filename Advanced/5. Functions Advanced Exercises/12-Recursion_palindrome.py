def find_potential(string, index):
    potential = ''
    if len(string) == 0:
        return potential
    index += 1
    potential += find_potential(string[index:], 0)
    potential += string[0]
    return potential


def palindrome(string, index=0):
    result = find_potential(string, index)
    if result == string:
        return f"{string} is a palindrome"
    else:
        return f"{string} is not a palindrome"


print(palindrome('kua', 0))