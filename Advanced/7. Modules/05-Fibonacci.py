from fibo import create, locate
while True:
    command = input()
    if command == 'Stop':
        break
    elif 'Create' in command:
        comm, seq, number = command.split()
        number = int(number)
        sequence = create(number)
        sequence = [str(x) for x in sequence]
        print(' '.join(sequence))
    elif 'Locate' in command:
        loc, number = command.split()
        number_to_locate = int(number)
        try:
            index = locate(number, sequence)
        except NameError:
            print('No sequence created, therefore, search is impossible. Create a sequence first by using the "Create Sequence" command.')
            continue
        if index is None:
            print(f'The number {number_to_locate} is not in the sequence')
        else:
            print(f'The number - {number_to_locate} is at index {index}')

