def even_odd(*args):
    args_list = list(args)
    command = args_list.pop()
    if command == 'odd':
        odd_nums = [int(x) for x in args_list if x % 2 == 1]
        return odd_nums
    else:
        even_nums = [int(x) for x in args_list if x % 2 == 0]
        return even_nums


print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))