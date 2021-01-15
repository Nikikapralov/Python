class Resources:
    def __init__(self):
        self.dictionary_items = {}
        self.data_input()

    def data_input(self):
        while True:
            resource_key = input()
            if resource_key == 'stop':
                print(self.print_output(self.dictionary_items))
                break
            amount_value = int(input())
            self.add_data_to_dict(resource_key, amount_value, self.dictionary_items)

    def add_data_to_dict(self, resource, amount, dictionary):
        if resource in dictionary:
            dictionary[resource] += amount
        else:
            dictionary[resource] = amount

    def print_output(self, dictionary):
        result = ''
        for key, value in dictionary.items():
            result += f'{key} -> {value}\n'
        return result


resources_1 = Resources()