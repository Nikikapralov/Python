tickets = input().split(', ')

def checking_left(left_half):
    previous_letter = ''
    contiguous = ''
    potential_win_left = ''
    first = True
    for letter in left_half:
        if first and (letter == '@' or letter == '#' or letter == '$' or letter == '^'):
            contiguous += letter
            previous_letter = letter
            first = False
        else:
            if previous_letter == letter:
                contiguous += letter
                if len(contiguous) >= 6:
                    potential_win_left = contiguous
            else:
                contiguous = ''
                if letter == '@' or letter == '#' or letter == '$' or letter == '^':
                    previous_letter = letter
                    contiguous += letter

    return potential_win_left

def checking_right(right_half):
    previous_letter = ''
    contiguous = ''
    potential_win_right = ''
    first = True
    for letter in right_half:
        if first and (letter == '@' or letter == '#' or letter == '$' or letter == '^'):
            contiguous += letter
            previous_letter = letter
            first = False
        else:
            if previous_letter == letter:
                contiguous += letter
                if len(contiguous) >= 6:
                    potential_win_right = contiguous
            else:
                contiguous = ''
                if letter == '@' or letter == '#' or letter == '$' or letter == '^':
                    previous_letter = letter
                    contiguous += letter

    return potential_win_right


for ticket in tickets:
    ticket = ticket.strip()
    if len(ticket) != 20:
        print('invalid ticket')
        continue
    else:
        half = int(len(ticket) / 2)
        left_half = ticket[:half]
        right_half = ticket[half:]
        potential_win_left = checking_left(left_half)
        potential_win_right = checking_right(right_half)
        if potential_win_left == '' or potential_win_right == '':
            print(f'ticket "{ticket}" - no match')
        elif potential_win_right == potential_win_left:
            if len(potential_win_right) == 10:
                print(f'ticket "{ticket}" - {len(potential_win_right)}{potential_win_right[0]} Jackpot!')
            else:
                print(f'ticket "{ticket}" - {len(potential_win_right)}{potential_win_right[0]}')
        else:
            if len(potential_win_right) >= 6 and len(potential_win_left) >= 6:
                if len(potential_win_left) > len(potential_win_right):
                    smaller = potential_win_right
                elif len(potential_win_left) < len(potential_win_right):
                    smaller = potential_win_left
                print(f'ticket "{ticket}" - {len(smaller)}{smaller[0]}')
            else:
                print(f'ticket "{ticket}" - no match')






