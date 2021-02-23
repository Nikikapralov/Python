n = int(input())
heroes_dict = {}
for _ in range(n):
    hero, hp, mp = input().split()
    heroes_dict.update({hero: {'MP': int(mp), 'HP': int(hp)}})
while True:
    command = input().split(' - ')
    if command[0] == 'End':
        break
    elif command[0] == 'CastSpell':
        hero_name = command[1]
        mp_needed = int(command[2])
        spell = command[3]
        hero_mp = int(heroes_dict[hero_name]['MP'])
        if hero_mp >= mp_needed:
            hero_mp -= mp_needed
            heroes_dict[hero_name]['MP'] = int(hero_mp)
            print(f'{hero_name} has successfully cast {spell} and now has {hero_mp} MP!')
        else:
            print(f'{hero_name} does not have enough MP to cast {spell}!')

    elif command[0] == 'TakeDamage':
        hero_name = command[1]
        damage = int(command[2])
        attacker = command[3]
        hero_HP = int(heroes_dict[hero_name]['HP'])
        hero_HP = hero_HP - damage
        if hero_HP <= 0:
            print(f'{hero_name} has been killed by {attacker}!')
            del heroes_dict[hero_name]
        else:
            heroes_dict[hero_name]['HP'] = hero_HP
            print(f'{hero_name} was hit for {damage} HP by {attacker} and now has {hero_HP} HP left!')

    elif command[0] == 'Recharge':
        hero_name = command[1]
        amount_mp = int(command[2])
        hero_mp = int(heroes_dict[hero_name]['MP'])
        new_mp = hero_mp + amount_mp
        if new_mp > 200:
            cut = new_mp - 200
            amount_mp -= cut
            hero_mp = 200
        else:
            hero_mp = new_mp
        print(f'{hero_name} recharged for {amount_mp} MP!')
        heroes_dict[hero_name]['MP'] = int(hero_mp)
    elif command[0] == 'Heal':
        hero_name = command[1]
        amount_HP = int(command[2])
        hero_HP = int(heroes_dict[hero_name]['HP'])
        new_HP = hero_HP + amount_HP
        if new_HP > 100:
            cut = new_HP - 100
            amount_HP -= cut
            hero_HP = 100
        else:
            hero_HP = new_HP
        print(f'{hero_name} healed for {amount_HP} HP!')
        heroes_dict[hero_name]['HP'] = int(hero_HP)

for key, value in sorted(heroes_dict.items(), key=lambda x: (-x[1]['HP'], x[0])):
    print(f'{key}')
    print(f"  HP: {value['HP']}")
    print(f"  MP: {value['MP']}")
