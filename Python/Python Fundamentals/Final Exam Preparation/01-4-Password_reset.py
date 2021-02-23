password = input()
while True:
    command = input().split()
    if command[0] == 'Done':
        break

    elif command[0] == 'TakeOdd':
        new_password = ''
        for index, char in enumerate(password):
            if index % 2 == 1:
                new_password += char
        password = new_password
        print(password)

    elif command[0] == 'Cut':
        index = int(command[1])
        length = int(command[2])
        end_index = index + length
        substring = password[index:end_index]
        password = password.replace(substring, '', 1)
        print(password)

    elif command[0] == 'Substitute':
        substring = command[1]
        substitute = command[2]
        if substring not in password:
            print('Nothing to replace!')
        else:
            password = password.replace(substring, substitute)
            print(password)

print(f'Your password is: {password}')