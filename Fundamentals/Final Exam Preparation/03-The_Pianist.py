n_pieces = int(input())
collection = {}
for _ in range(n_pieces):
    piece, composer, key = input().split('|')
    collection[piece] = []
    collection[piece].append(composer)
    collection[piece].append(key)
while True:
    command = input()
    if command == 'Stop':
        break
    elif 'Add' in command:
        action, piece, composer, key = command.split('|')
        if piece in collection:
            print(f'{piece} is already in the collection!')
        elif piece not in collection:
            collection[piece] = []
            collection[piece].append(composer)
            collection[piece].append(key)
            print(f'{piece} by {composer} in {key} added to the collection!')
    elif 'Remove' in command:
        action, piece = command.split('|')
        if piece in collection:
            collection.pop(piece)
            print(f'Successfully removed {piece}!')
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.')
    elif 'ChangeKey' in command:
        action, piece, new_key = command.split('|')
        if piece in collection:
            collection[piece][1] = new_key
            print(f'Changed the key of {piece} to {new_key}!')
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.')
for key_1, value_1 in sorted(collection.items(), key=lambda x: (x[0], x[1][0])):
    print(f'{key_1} -> Composer: {value_1[0]}, Key: {value_1[1]}')
