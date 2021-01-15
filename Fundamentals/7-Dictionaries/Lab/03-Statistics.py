class Stock:
    def __init__(self):
        self.key = None
        self.value = None
        self.dict_stock = {}
        self.all_products = None
        self.quantity = None

    def incoming_products(self):
        while True:
            command = input()
            if command == 'statistics':
                self.print_result()
                return
            else:
                key_value_pairs = command.split(': ')
            self.add_product_to_dict_stock(key_value_pairs)

    def add_product_to_dict_stock(self, key_value_pair):
        self.key = key_value_pair[0]
        self.value = int(key_value_pair[1])
        if self.key in self.dict_stock:
            self.dict_stock[self.key] += self.value
        else:
            self.dict_stock.update({self.key: self.value})

    def print_result(self):
        print('Products in stock:')
        for key, value in self.dict_stock.items():
            print(f"- {key}: {value}")
        print(self.total_products())
        print(self.total_quantity())

    def total_products(self):
        self.all_products = len(self.dict_stock)
        return f'Total Products: {self.all_products}'

    def total_quantity(self):
        flag = False
        for key, value in self.dict_stock.items():
            int_value = int(value)
            if flag:
                self.quantity += int_value
            else:
                self.quantity = int_value
                flag = True

        return f'Total Quantity: {self.quantity}'


stock_1 = Stock()
stock_1.incoming_products()
