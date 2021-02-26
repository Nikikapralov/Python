import os
path = r''
data = os.listdir(path)
dictionary = {}
for item in data:
    name, extension = item.split('.')
    if extension not in dictionary:
        dictionary[extension] = [name + '.' + extension]
    else:
        dictionary[extension].append(name + '.' + extension)
sorted_dict = sorted(dictionary.items(), key=lambda x: (x[0], x[1]))
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
with open(desktop + '\\' + 'report.txt', 'w') as file_write:
    for tupple in sorted_dict:
        typpe = tupple[0]
        name_files = tupple[1]
        file_write.writelines(f'.{typpe}\n')
        for curr_file in name_files:
            file_write.writelines(f'---{curr_file}\n')