import sys
experience_needed = float(input())
count_of_battles = int(input())
experience = 0
for battle in range(1, count_of_battles + 1):
    experience_earned = float(input())
    if battle % 3 == 0:
        bonus = experience_earned * 0.15
        experience += (experience_earned + bonus)
    elif battle % 5 == 0:
        bonus = experience_earned * 0.10
        experience += (experience_earned - bonus)
    elif battle % 15 == 0:
        bonus = experience_earned * 0.05
        experience += (experience_earned + bonus)
    else:
        experience += experience_earned
    if experience >= experience_needed:
        print(f'Player successfully collected his needed experience for {battle} battles.')
        sys.exit()
experience_left = experience_needed - experience
print(f'Player was not able to collect the needed experience, {experience_left:.2f} more needed.')


