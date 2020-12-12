a = int(input())
b = int(input())
c = int(input())
percent_taken_density = float(input())

v_aquarium = a * b * c
v_taken_of_other_stuff = v_aquarium * percent_taken_density / 100
v_taken_of_water_cm3 = v_aquarium - v_taken_of_other_stuff

#1cm*1cm*1cm 1dm^3 = 10cm * 10cm *10cm
#1dm^3 = 1000cm^3
v_taken_of_water_dm3 = v_taken_of_water_cm3 / 1000
print(v_taken_of_water_dm3)