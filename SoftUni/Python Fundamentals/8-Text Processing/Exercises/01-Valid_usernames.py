list_users = input().split(', ')
result = []

for username in list_users:
    counter = 0
    condition_1 = False
    if 3 < len(username) < 16:
        condition_1 = True
    condition_2 = False
    for letter in username:
        if not letter.isdigit() and not letter.isalpha() and letter != '-' and letter != '_':
            continue
        else:
            counter += 1
            if counter == len(username):
                condition_2 = True
    if condition_1 and condition_2:
        result.append(username)

for item in result:
    print(item)
