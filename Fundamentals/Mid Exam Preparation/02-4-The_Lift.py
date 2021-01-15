people_queue = int(input())
state_of_elevator = [int(state) for state in input().split()]
Flag = False
for index_wagon in range(len(state_of_elevator)):
    if Flag:
        break
    while True:
        if state_of_elevator[index_wagon] == 4:
            break
        else:
            if people_queue == 0:
                Flag = True
                break
            people_queue -= 1
            state_of_elevator[index_wagon] += 1
            if people_queue == 0:
                Flag = True
                break
str_state_of_elevator = [str(item) for item in state_of_elevator]
output = " ".join(str_state_of_elevator)
if Flag:
    print('The lift has empty spots!')
    print(output)
if not Flag:
    print(f"There isn't enough space! {people_queue} people in a queue!")
    print(output)