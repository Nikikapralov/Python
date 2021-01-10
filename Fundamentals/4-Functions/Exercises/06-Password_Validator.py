def password_validator(password):
    Flag = True
    digit_counter = 0
    print_counter = 0
    if not 6 <= len(password) <= 10:
        print('Password must be between 6 and 10 characters')
        Flag = False
    for char in password:
        if char.isdigit():
            digit_counter += 1
        if ord(char) in range(90, 96) or ord(char) in range(122, 126) or ord(char) in range(-1, 47) or ord(char) in range(57, 64):
            if print_counter > 0:
                continue
            print('Password must consist only of letters and digits')
            print_counter += 1
            Flag = False
    if digit_counter < 2:
        print('Password must have at least 2 digits')
        Flag = False
    if Flag:
        password_is_valid = print('Password is valid')
        return password_is_valid


password = input()
execute = password_validator(password)