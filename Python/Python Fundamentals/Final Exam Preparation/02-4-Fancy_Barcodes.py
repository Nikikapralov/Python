import re
pattern = r'^@#+[A-Z][a-zA-Z0-9]{4,}[A-Z]@#+$'
repeats = int(input())
for _ in range(repeats):
    barcode = input()
    match = re.findall(pattern, barcode)
    if match:
        current_group = ''
        Flag = False
        for code in match:
            for item in code:
                if item.isdigit():
                    current_group += item
                    Flag = True
            if not Flag:
                current_group = '00'
        print(f'Product group: {current_group}')
    elif not match:
        print('Invalid barcode')