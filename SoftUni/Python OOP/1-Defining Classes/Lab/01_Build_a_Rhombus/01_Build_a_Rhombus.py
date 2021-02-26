def build():
    size = get_size()
    exception(size)
    upper_part = build_upper(size)
    middle_part = build_middle(size)
    lower_part = build_lower(size)
    rhombus = construct(upper_part, middle_part, lower_part)
    print(rhombus)


def get_size():
    size = int(input())
    return size


def build_upper(size):
    upper_part = (size - 1) * ' ' + '*' + '\n'

    for i in range(2, size):
        upper_part += (size - i - 1) * ' ' + i * ' *' + '\n'

    return upper_part


def build_middle(size):
    middle_part = '*' + (size - 1) * ' *' + '\n'
    return middle_part


def build_lower(size):
    lower_part = ''

    for i in range(size - 1, 1, -1):
        lower_part += (size - i - 1) * ' ' + i * ' *' + '\n'

    lower_part += (size - 1) * ' ' + '*'
    return lower_part


def construct(upper_part, middle_part, lower_part):
    rhombus = upper_part + middle_part + lower_part
    return rhombus


def exception(size):
    if size == 1:
        print('*')
        exit()
    elif size == 0:
        print()
        exit()
    return


build()
