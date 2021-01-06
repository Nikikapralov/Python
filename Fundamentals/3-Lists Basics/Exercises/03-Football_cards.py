list_cards = input().split()
team_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

team_a_counter = 11
team_b_counter = 11

for card in list_cards:
    tokens = card.split("-")
    team = tokens[0]
    player = int(tokens[1])
    if team == "A":
        if player in team_a:
            team_a.remove(player)
            team_a_counter -= 1
    elif team == "B":
        if player in team_b:
            team_b.remove(player)
            team_b_counter -= 1
    if team_a_counter < 7 or team_b_counter < 7:
        break
print(f"Team A - {team_a_counter}; Team B - {team_b_counter}")
if team_a_counter < 7 or team_b_counter < 7:
    print(f"Game was terminated")




cards = input()
team_A_kicked = []
team_B_kicked = []
list_cards = cards.split()
counter_A = 0
counter_B = 0
Flag = False
for value in list_cards:
    if counter_A == 5 or counter_B == 5:
        break
    if 'A' in value:
        for i in range(1, 12):
            if i in team_A_kicked:
                continue
            i = str(i)
            if i in value:
                i = int(i)
                team_A_kicked.append(i)
                counter_A += 1
                break
    elif 'B' in value:
        for i in range(1, 12):
            if i in team_B_kicked:
                continue
            i = str(i)
            if i in value:
                i = int(i)
                team_B_kicked.append(i)
                counter_B += 1
                break
total_players_A = 11 - counter_A
total_players_B = 11 - counter_B
print(f'Team A - {total_players_A}; Team B - {total_players_B}')
if counter_B == 5 or counter_A == 5:
    print('Game was terminated')