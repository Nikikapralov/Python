import re
n_inputs = int(input())
pattern = r'(\*|@)(?P<tag>[A-Z][a-z]{2,})(\1):\s(?P<message>\[[A-Za-z]\]\|\[[A-Za-z]\]\|\[[A-Za-z]\]\|)$'
for _ in range(n_inputs):
    potential_message = input()
    result = re.finditer(pattern, potential_message)
    if not list(result):
        print('Valid message not found!')
        continue
    else:
        result = re.finditer(pattern, potential_message)
        encrypted_letters = []
        for item in result:
            tag = item.group('tag')
            message = item.group('message')
            for char in message:
                if char.isalpha():
                    encrypted_letters.append(str(ord(char)))
        print(f'{tag}: {" ".join(encrypted_letters)}')



