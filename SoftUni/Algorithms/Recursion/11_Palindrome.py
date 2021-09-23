def palindrome(string):
    def reverse(string):
        if not string:
            return ""
        return string[-1] + reverse(string[:len(string) - 1])
    if string == reverse(string):
        return True
    return False

print(palindrome("tacocat"))