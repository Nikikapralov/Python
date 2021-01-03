number_of_chars = int(input())
sum = 0
for i in range(number_of_chars):
    spec_char = input()
    spec_char_ascii = ord(spec_char)
    sum += spec_char_ascii
print(f'The sum equals: {sum}')