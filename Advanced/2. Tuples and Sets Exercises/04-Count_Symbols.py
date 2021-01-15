data = input()
unique_chars = set()
[unique_chars.add(char) for char in data]
chars_count_dict = {}
[chars_count_dict.update({char: data.count(char)}) for char in unique_chars]
[print(f'{key}: {value} time/s') for key, value in sorted(chars_count_dict.items(), key=lambda x: x[0], reverse=False)]
