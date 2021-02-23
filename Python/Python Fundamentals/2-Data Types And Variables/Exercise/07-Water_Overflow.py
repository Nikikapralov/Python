capacity = 255
rest_capacity = capacity
total_liters = 0
number_of_infusions = int(input())
for i in range(number_of_infusions):
    liters_of_water_per_infusion = int(input())
    if liters_of_water_per_infusion <= 0:
        continue
    rest_capacity -= liters_of_water_per_infusion
    total_liters += liters_of_water_per_infusion
    if rest_capacity < 0:
        total_liters -= liters_of_water_per_infusion
        rest_capacity += liters_of_water_per_infusion
        print('Insufficient capacity!')
print(total_liters)