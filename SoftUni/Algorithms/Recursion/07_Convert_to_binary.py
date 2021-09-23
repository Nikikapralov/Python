def bin_con(number):
    assert int(number) == number, "Only integers!"
    if number == 1 or number == -1:
        return 1
    return str(bin_con(number // 2)) + str(number % 2)


print(bin_con(-1))