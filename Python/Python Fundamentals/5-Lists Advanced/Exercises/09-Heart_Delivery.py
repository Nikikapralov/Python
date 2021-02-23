neighborhood = [int(house) for house in input().split('@')]
cupid_position_index = 0
valentine_day_list = []
while True:
    command = [int(item) if item.isdigit() else str(item) for item in input().split()]
    if 'Love!' in command:
        break
    else:
        length = command[1]
        cupid_position_index += length
        if cupid_position_index > len(neighborhood) - 1:
            cupid_position_index = 0
        if neighborhood[cupid_position_index] == 0:
            print(f"Place {cupid_position_index} already had Valentine's day.")
        else:
            neighborhood[cupid_position_index] -= 2
            if neighborhood[cupid_position_index] == 0:
                print(f"Place {cupid_position_index} has Valentine's day.")
                valentine_day_list.append(0)
print(f"Cupid's last position was {cupid_position_index}.")
if len(valentine_day_list) == len(neighborhood):
    print('Mission was successful.')
else:
    failed_house = len(neighborhood) - len(valentine_day_list)
    print(f'Cupid has failed {failed_house} places.')

