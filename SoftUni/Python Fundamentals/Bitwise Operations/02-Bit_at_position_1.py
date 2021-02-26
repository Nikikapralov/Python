number = int(input())
bin_number = bin(number)
POSITION = 1
bin_shifted = number >> POSITION
if bin_shifted & 1:
    print(1)
else:
    print(0)

