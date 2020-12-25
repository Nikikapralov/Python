width = int(input())
length = int(input())
size_of_cake = width * length
difference = 0
total_number_of_pieces_taken = 0
while True:
    number_of_pieces_taken = input()
    if number_of_pieces_taken == "STOP":
        if difference == 0:
            print(f'{size_of_cake} pieces are left.')
        else:
            print(f'{difference} pieces are left.')
        break
    else:
        number_of_pieces_taken = int(number_of_pieces_taken)
        total_number_of_pieces_taken += number_of_pieces_taken
        difference = abs(size_of_cake - total_number_of_pieces_taken)
    if total_number_of_pieces_taken >= size_of_cake:
        print(f'No more cake left! You need {difference} pieces more.')
        break


