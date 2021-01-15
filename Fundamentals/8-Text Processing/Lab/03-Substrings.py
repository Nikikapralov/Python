substring = input()
string = input()
result = string
while substring in result:
    result = result.replace(substring, '')

print(result)
