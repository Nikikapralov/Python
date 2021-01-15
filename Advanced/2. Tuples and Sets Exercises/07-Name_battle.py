lines = int(input())
odd = set()
even = set()
for line in range(1, lines + 1):
    name = input()
    sums = 0
    result = 0
    for letter in name:
        sums += ord(letter)
        result = sums // line
    if result % 2 == 0:
        even.add(result)
    else:
        odd.add(result)
summed_odd = sum(odd)
summed_even = sum(even)
if summed_odd == summed_even:
    result = [str(value) for value in odd.union(even)]
elif summed_odd > summed_even:
    result = [str(value) for value in odd.difference(even)]
else:
    result = [str(value) for value in odd.symmetric_difference(even)]

print(", ".join(result))
