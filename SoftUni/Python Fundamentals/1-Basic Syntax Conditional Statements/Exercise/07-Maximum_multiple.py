Divisor = int(input())
Bound = int(input())
for N in range(Bound, 0, -1):
    if N % Divisor == 0:
        break
print(N)
