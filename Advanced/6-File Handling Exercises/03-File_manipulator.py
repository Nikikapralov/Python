import os
path = r''


def create(name, path):
   file = open(path + "\\" + name, 'w')
   file.close()


def add(name, content, path):
    with open(path + "\\" + name, 'a') as file:
        file.write(content)
        file.write('\n')


def replace(name, old, new, path):
    try:
        with open(path + "\\" + name, 'r') as file:
            data = file.read()
            data = data.replace(old, new)
        with open(path + "\\" + name, 'w') as file:
            file.write(data)

    except FileNotFoundError:
        print('An error occurred')


def delete(name, path):
    try:
        os.remove(path + "\\" + name)
    except FileNotFoundError:
        print('An error occurred')


while True:
    command = input().split('-')
    if 'End' in command:
        break
    elif 'Create' in command:
        name = command[1]
        create(name, path)
    elif 'Add' in command:
        name = command[1]
        content = command[2]
        add(name, content, path)
    elif 'Replace' in command:
        name = command[1]
        old = command[2]
        new = command[3]
        replace(name, old, new, path)
    elif 'Delete' in command:
        name = command[1]
        delete(name, path)