print([x for x in range(int(input()), int(input()) + 1) if any([x % y == 0 for y in range(2, 11)])])
