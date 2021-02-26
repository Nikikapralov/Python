version = input().split('.')
int_version = [int(x) for x in version]
if int_version[2] == 9:
    int_version[2] -= 9
    int_version[1] += 1
else:
    int_version[2] += 1

if int_version[1] == 10:
    int_version[1] -= 10
    int_version[0] += 1

print(f'{int_version[0]}.{int_version[1]}.{int_version[2]}')

