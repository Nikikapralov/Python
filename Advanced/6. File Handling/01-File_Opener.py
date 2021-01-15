path = r''
try:
    file = open(path, 'r')
    print('File found')
except FileNotFoundError:
    print('File not found')

