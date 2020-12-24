name = input()
password = input()
password_entry = input()

while password_entry != password:
    password_entry = input()

print(f'Welcome {name}!')