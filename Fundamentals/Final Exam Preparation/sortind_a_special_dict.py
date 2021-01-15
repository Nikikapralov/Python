dict_1 = {'ABCDEFG': 'AB', 'GFE': 'AC'}
sorted_1 = sorted(dict_1.items(), key=lambda x: (x[1], [-ord(x[0][n]) for n in range(len(x[0]))]), reverse=False)
print(sorted_1)

