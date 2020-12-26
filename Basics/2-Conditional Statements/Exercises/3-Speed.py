skorost = float(input())

if skorost <= 10:
    print('slow')
elif skorost <= 50:
    print('average')
elif skorost <= 150:
    print('fast')
elif skorost <= 1000:
    print('ultra fast')
elif skorost > 1000:
    print('extremely fast')