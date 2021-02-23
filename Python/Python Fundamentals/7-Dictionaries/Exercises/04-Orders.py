class Order:
    def __init__(self):
        self.dict_items = {}
        self.filling_the_dict(self.dict_items)

    def filling_the_dict(self, dictionary):
        while True:
            command = input()
            if command == 'buy':
                break
            name_key, price_value, quantity_value = command.split()
            price_value = float(price_value)
            quantity_value = int(quantity_value)
            if name_key not in dictionary:
                dictionary[name_key] = [price_value, quantity_value]
            else:
                dictionary[name_key][1] += quantity_value
                if dictionary[name_key][0] != price_value:
                    dictionary[name_key][0] = price_value
        print(self.print_output(self.dict_items))

    def print_output(self, dictionary):
        result = ''
        for key, value_list_data in dictionary.items():
            product = key
            price = value_list_data[0]
            quantity = value_list_data[1]
            total_price = price * quantity
            result += f'{product} -> {total_price:.2f}\n'
        return result


order_1 = Order()

