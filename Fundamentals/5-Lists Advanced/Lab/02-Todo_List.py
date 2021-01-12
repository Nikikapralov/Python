def todo_list():
    result = []
    to_do_final = [0 for _ in range(10)]
    while True:
        to_do = input().split('-')
        if 'End' in to_do:
            break
        importance = int(to_do[0])
        value = to_do[1]
        to_do_final.pop(importance - 1)
        to_do_final.insert(importance - 1, value)
    to_do_final_for_real_this_time = [result.append(item) for item in to_do_final if not item == 0]
    return result




execute = todo_list()
print(execute)