message = input()
command = input()
while command != 'Reveal':
    data = command.split(':|:')
    if data[0] == "InsertSpace":
        index = int(data[1])
        new_message = message[:index] + ' ' + message[index:]
        message = new_message
        print(message)
    elif data[0] == 'Reverse':
        substring = data[1]
        if substring in message:
            start_index = message.find(substring)
            end_index = start_index + len(substring)
            rev_substring = substring[::-1]
            new_message = message[:start_index] + message[end_index:] + rev_substring
            message = new_message
            print(message)
        else:
            print('error')
    elif data[0] == 'ChangeAll':
        old_string = data[1]
        new_string = data[2]
        new_message = message.replace(old_string, new_string)
        message = new_message
        print(message)
    command = input()
print(f'You have a new text message: {message}')