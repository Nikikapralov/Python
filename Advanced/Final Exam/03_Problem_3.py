from collections import deque


def stock_availability(inventory_list, command, *args):
    inventory_list = deque(inventory_list)
    if command == 'delivery':
        inventory_list.extend(args)
    elif command == 'sell':
        if args:
            token = args[0]
            if type(token) is int:
                for box in range(token):
                    inventory_list.popleft()
            else:
                for token in args:
                    while token in inventory_list:
                        inventory_list.remove(token)
        else:
            inventory_list.popleft()
    return list(inventory_list)





print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
