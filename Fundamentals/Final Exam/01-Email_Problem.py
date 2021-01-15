email = input()
while True:
    command = input()
    if command == 'Complete':
        break
    elif command == 'Make Upper':
        email = email.upper()
        print(email)
    elif command == 'Make Lower':
        email = email.lower()
        print(email)
    elif 'GetDomain' in command:
        data = command.split()
        count = int(data[1])
        start_index = len(email) - count
        last_count_chars = email[start_index:]
        print(last_count_chars)
    elif command == 'GetUsername':
        if '@' in email:
            index = email.find('@')
            username = email[:index]
            print(username)
        elif '@' not in email:
            print(f"The email {email} doesn't contain the @ symbol.")
    elif 'Replace' in command:
        data = command.split()
        substring = data[1]
        email = email.replace(substring, '-')
        print(email)
    elif command == 'Encrypt':
        for char in email:
            asci = ord(char)
            print(asci, end=' ')

