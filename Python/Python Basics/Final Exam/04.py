import math
starting_population = int(input())
years = int(input())
total_population = starting_population
born_bees = 0
dead_bees = 0
bees_who_leave = 0
for i in range(1, years + 1):
    is_it_a_5th_year = i % 10 == 0 or i % 10 == 5
    born_bees = math.floor(total_population / 10) * 2
    total_population += born_bees
    if is_it_a_5th_year:
        bees_who_leave = math.floor(total_population / 50) * 5
        total_population -= bees_who_leave
    dead_bees = math.floor(total_population / 20) * 2
    total_population -= dead_bees

print(f'Beehive population: {total_population}')
