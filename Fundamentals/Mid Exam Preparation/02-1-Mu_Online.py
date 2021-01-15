health = 100
bitcoins = 0
dungeon_rooms = input().split('|')
room_counter = 0
Flag = True
for room in dungeon_rooms:
    room_counter += 1
    room_split = room.split()
    command = room_split[0]
    if command == 'potion':
        health_to_heal = int(room_split[1])
        health += health_to_heal
        if health > 100:
            health_that_got_left_out = health - 100
            health = 100
            health_i_actually_healed_for = health_to_heal - health_that_got_left_out
            health_to_heal = health_i_actually_healed_for
        print(f'You healed for {health_to_heal} hp.')
        print(f'Current health: {health} hp.')
    elif command == 'chest':
        bitcoins_found = int(room_split[1])
        bitcoins += bitcoins_found
        print(f'You found {bitcoins_found} bitcoins.')
    else:
        monster = room_split[0]
        monster_attack = int(room_split[1])
        health -= monster_attack
        if health <= 0:
            print(f'You died! Killed by {monster}.')
            print(f'Best room: {room_counter}')
            Flag = False
            break
        else:
            print(f'You slayed {monster}.')

if Flag:
    print(f"You've made it!")
    print(f'Bitcoins: {bitcoins}')
    print(f'Health: {health}')
