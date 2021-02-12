tasks = [int(x) for x in input().split(', ')]
indexes = [int(x) for x in range(len(tasks))]
tasks_indexes = sorted(zip(tasks, indexes), key=lambda x: x[0])
index_searched = int(input())
searched_for = tasks[index_searched]
result = 0
for task, index in tasks_indexes:
    result += task
    if task == searched_for:
        if index == index_searched:
            break
print(result)
