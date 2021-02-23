max_amount_of_stars = int(input())
for stars_on_top in range(1, max_amount_of_stars + 1):
    print('*' * stars_on_top)
for stars_on_bottom in range(max_amount_of_stars - 1, 0, -1):
    print('*' * stars_on_bottom)