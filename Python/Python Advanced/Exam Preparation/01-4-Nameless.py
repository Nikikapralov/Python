from collections import deque
males = deque([int(x) for x in input().split()])
females = deque([int(x) for x in input().split()])
matches = 0
while True:
    if not males or not females:
        break
    first_female = females.popleft()
    last_male = males.pop()
    if first_female <= 0:
        males.append(last_male)
        continue
    elif last_male <= 0:
        females.appendleft(first_female)
        continue
    elif last_male % 25 == 0:
        males.pop()
        females.appendleft(first_female)
        continue
    elif first_female % 25 == 0:
        females.popleft()
        males.append(last_male)
        continue
    elif first_female == last_male:
        matches += 1
        continue
    else:
        males.append(last_male - 2)

print(f'Matches: {matches}')
if not males:
    print(f'Males left: none')
else:
    print(f'Males left: {", ".join([str(male) for male in reversed(males)])}')

if not females:
    print(f'Females left: none')
else:
    print(f'Females left: {", ".join([str(female) for female in females])}')
