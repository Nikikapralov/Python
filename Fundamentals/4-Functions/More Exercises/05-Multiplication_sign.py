nums = 3
product = 'positive'
is_zero = False
minus_checks = 0
for _ in range(nums):
    current_num = int(input())
    if is_zero:
        continue
    if current_num < 0:
        product = 'negative'
        minus_checks += 1
    elif current_num == 0:
        product = 'zero'
        is_zero = True
if product != 'zero':
    if minus_checks % 2 == 0:
        product = 'positive'
print(product)

