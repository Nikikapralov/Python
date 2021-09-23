def reverse(string):
    if not string:
        return ""
    return string[-1] + reverse(string[:len(string) - 1])
print(reverse("python"))