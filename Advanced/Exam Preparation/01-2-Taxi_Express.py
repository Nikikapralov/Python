from collections import deque
customers = deque([int(customer) for customer in input().split(', ')])
taxis = deque([int(taxi) for taxi in input().split(', ')])
total_time = 0
while customers:
    if not taxis and customers:
        print('Not all customers were driven to their destinations')
        print(f'Customers left: {", ".join([str(x) for x in customers])}')
        exit()
    current_customer = customers.popleft()
    current_taxi = taxis.pop()
    if current_taxi >= current_customer:
        total_time += current_customer
    else:
        customers.appendleft(current_customer)
print(f'All customers were driven to their destinations')
print(f'Total time: {total_time} minutes')