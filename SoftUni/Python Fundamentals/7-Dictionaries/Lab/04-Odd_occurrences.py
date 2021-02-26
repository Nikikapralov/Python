class Occurrence:
    def __init__(self, data):
        self.data = data.split()
        self.dict_data = {}
        self.final_dict = {}
        self.filling_the_dict()

    def filling_the_dict(self):
        for item in self.data:
            key_all_lowercase = item.lower()
            if key_all_lowercase in self.dict_data:
                self.dict_data[key_all_lowercase] += 1
            else:
                key = key_all_lowercase
                value = 1
                self.dict_data.update({key: value})
        self.odd_or_even_count()

    def odd_or_even_count(self):
        for key, value in self.dict_data.items():
            if value % 2 == 1:
                self.final_dict.update({key: value})

    def print_result(self):
        output_keys = self.final_dict.keys()
        output = ' '.join(output_keys)
        return output


occurrence_1 = Occurrence(input())
print(occurrence_1.print_result())
