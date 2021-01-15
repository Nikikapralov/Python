rows, columns = [int(x) for x in input().split(', ')]
matrix = []
total_sum = 0
for _ in range(int(rows)):
    row = [int(item) for item in input().split(', ')]
    if len(row) < columns:
        while len(row) != columns:
            row.append(0)
    total_sum += sum(row)
    matrix.append(row)

print(total_sum)
print(matrix)