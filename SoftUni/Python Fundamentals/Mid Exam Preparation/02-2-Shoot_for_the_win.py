targets = [int(target) for target in input().split()]
count_of_shot = 0
while True:
    index_to_shoot = input()
    if index_to_shoot == 'End':
        break
    index_to_shoot = int(index_to_shoot)
    if index_to_shoot not in range(len(targets)):
        continue
    else:
        current_target = targets[index_to_shoot]
        if current_target == - 1:
            continue
        for index_of_item in range(len(targets)):
            if targets[index_of_item] == -1:
                continue
            if targets[index_of_item] <= current_target:
                targets[index_of_item] += current_target
            elif targets[index_of_item] > current_target:
                targets[index_of_item] -= current_target
        targets[index_to_shoot] = -1
        count_of_shot += 1
targets_str = [str(x) for x in targets]
targets_joined = ' '.join(targets_str)
print(f"Shot targets: {count_of_shot} -> {targets_joined}")



