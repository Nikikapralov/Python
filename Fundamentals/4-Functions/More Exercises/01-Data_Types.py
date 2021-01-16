def get_command():
    command = input()
    return command


def command_int():
    number = int(input())
    result = number * 2
    return result


def command_real():
    number = float(input())
    result = number * 1.5
    return f'{result:.2f}'


def command_string():
    string = input()
    result = f'${string}$'
    return result


command = get_command()
if command == 'int':
    print(command_int())
elif command == 'real':
    print(command_real())
else:
    print(command_string())
