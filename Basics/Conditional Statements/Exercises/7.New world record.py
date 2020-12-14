import math
current_record = float(input())
distance = float(input())
time_for_1m = float(input())
# suprotivlenie = na vseki 15 metra go zabavia s 12.5s
time_for_distance = distance * time_for_1m
how_many_times_is_he_slowed_by_water = math.floor(distance / 15)
lost_time_from_water = how_many_times_is_he_slowed_by_water * 12.5
true_time = time_for_distance + lost_time_from_water
seconds_slower = current_record - true_time

if true_time < current_record:
    print(f'Yes, he succeeded! The new world record is {true_time:.2f} seconds.')

elif true_time >= current_record:
    print(f'No, he failed! He was {abs(seconds_slower):.2f} seconds slower.')