import sys
number_of_snowballs = int(input())
highest_value = -sys.maxsize
best_quality = 0
best_time = 0
best_snow = 0
for i in range(number_of_snowballs):
    snow = int(input())
    time = int(input())
    quality = int(input())
    snowball_value = int(snow / time)
    snowball_value = snowball_value ** quality
    if snowball_value > highest_value:
        highest_value = snowball_value
        best_quality = quality
        best_snow = snow
        best_time = time
print(f'{best_snow} : {best_time} = {highest_value} ({best_quality})')