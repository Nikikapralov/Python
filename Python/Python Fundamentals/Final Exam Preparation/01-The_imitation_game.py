code = input()
while True:
    command = input()
    if command == 'Decode':
        break
    elif 'Move' in command:
        action, n_letters = command.split('|')
        n_letters = int(n_letters)
        string_to_move = code[0:n_letters]
        string_without_n_letters = code[n_letters:]
        final_string = string_without_n_letters + string_to_move
        code = final_string
    elif 'Insert' in command:
        action, index, value = command.split('|')
        index = int(index)
        final_string = code[0:index] + value + code[index:]
        code = final_string
    elif 'ChangeAll' in command:
        action, substring, replacement = command.split('|')
        code = code.replace(substring, replacement)

print(f'The decrypted message is: {code}')
