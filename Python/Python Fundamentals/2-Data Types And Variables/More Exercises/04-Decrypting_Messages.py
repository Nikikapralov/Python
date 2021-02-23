key = int(input())
n_chars = int(input())
decrypted_word = ''
for _ in range(n_chars):
    char = input()
    decrypted_char = chr(ord(char) + key)
    decrypted_word += decrypted_char
print(decrypted_word)