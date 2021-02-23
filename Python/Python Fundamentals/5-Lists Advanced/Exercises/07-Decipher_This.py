secret_message = [word for word in input().split()]
number = []
trash = [number.append(letter) if letter.isdigit() else number.append(' ')for word_1 in secret_message for letter in word_1]
first_letter = ''.join(number)
numbers_final = [int(number) for number in first_letter.split(' ') if number != '']
letters = [chr(number_1) for number_1 in numbers_final]
letters_1 = []
removing = [letters_1.append(char) if not char.isdigit() else letters_1.append(' ') for word_2 in secret_message for char in word_2]
almost_final_letters = ''.join(letters_1)
letters_final = [letter for letter in almost_final_letters.split(' ') if letter != '']
final = [letter for letter in letters]
index = -1
final_for_real = []
for word_3 in letters_final:
    index += 1
    word_3 = list(word_3)
    word_3[0], word_3[-1] = word_3[-1], word_3[0]
    word_final = ''.join(word_3)
    result = final[index] + word_final
    final_for_real.append(result)
print(' '.join(final_for_real))

