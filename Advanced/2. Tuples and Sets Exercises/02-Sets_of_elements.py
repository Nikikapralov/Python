n, m = input().split()
n_set = set()
m_set = set()
[n_set.add(input()) for _ in range(int(n))]
[m_set.add(input()) for _ in range(int(m))]
result = n_set.intersection(m_set)
[print(item) for item in result]
