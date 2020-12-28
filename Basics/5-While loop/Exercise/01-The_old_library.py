Book_Ani_Searches_For = input()
Books_Checked = 0
while True:
    Book_Ani_Finds = input()
    if Book_Ani_Searches_For == Book_Ani_Finds:
        print(f'You checked {Books_Checked} books and found it.')
        break
    elif Book_Ani_Finds == 'No More Books':
        print('The book you search is not here!')
        print(f'You checked {Books_Checked} books.')
        break
    else:
        Books_Checked += 1
        continue