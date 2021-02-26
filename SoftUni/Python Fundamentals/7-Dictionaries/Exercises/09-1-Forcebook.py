jedi = {}
result = {}
while True:
    command = input()
    if command == 'Lumpawaroo':
        break

    if '|' in command:
        side_value, user_key = command.split(' | ')
        if user_key not in jedi:
            jedi[user_key] = side_value

    elif '->' in command:
        user_to_change, side_to_change_to = command.split(' -> ')
        jedi[user_to_change] = side_to_change_to

        print(f"{user_to_change} joins the {side_to_change_to} side!")

for key, value in jedi.items():
    if value not in result:
        result[value] = [key]
    else:
        result[value].append(key)

for key, value in sorted(result.items(), key=lambda x: (-len(x[1]), x[0])):
    print(f'Side: {key}, Members: {len(value)}')
    for item in sorted(value):
        print(f'! {item}')















