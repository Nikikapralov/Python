amount_queries = int(input())
stack_of_queries = []
for _ in range(amount_queries):
    command = input().split()
    if command[0] == '1':
        stack_of_queries.append(int(command[1]))
    elif command[0] == '2':
        try:
            stack_of_queries.pop()
        except IndexError:
            continue
    elif command[0] == '3':
        try:
            print(max(stack_of_queries))
        except ValueError:
            continue
    elif command[0] == '4':
        try:
            print(min(stack_of_queries))
        except ValueError:
            continue

stack_of_queries = stack_of_queries[::-1]
print(*stack_of_queries, sep=', ')
