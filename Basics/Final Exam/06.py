import sys
needed_honey_for_winter = float(input())
name_of_bee = input()
sum_of_honey = 0
honey_gathered = 0
honey_surplus = 0
honey_needed = 0
if needed_honey_for_winter >= 0:
    while name_of_bee != 'Winter has come':
        for i in range(6):
            honey_gathered = float(input())
            sum_of_honey += honey_gathered
        if sum_of_honey < 0:
            print(f'{name_of_bee} was banished for gluttony')
        elif sum_of_honey >= needed_honey_for_winter:
            break
        name_of_bee = input()

    if sum_of_honey >= needed_honey_for_winter:
        honey_surplus = sum_of_honey - needed_honey_for_winter
        print(f'Well done! Honey surplus {honey_surplus:.2f}.')
    elif sum_of_honey <= needed_honey_for_winter:
        honey_needed = needed_honey_for_winter - sum_of_honey
        print(f'Hard Winter! Honey needed {honey_needed:.2f}.')



