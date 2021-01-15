class Farming:
    def __init__(self):
        self.dict_data = {}
        self.motes = 0
        self.shards = 0
        self.fragments = 0
        self.legendary_item = None
        self.flag = False
        self.result = ''
        print(self.add_to_dict(self.dict_data))


    def add_to_dict(self, dictionary):
        dictionary.update({'fragments': 0, 'shards': 0, 'motes': 0})
        while True:
            data = input().split()
            for item in range(len(data)):
                if item % 2 == 0:
                    amount = int(data[item])
                else:
                    resource = data[item]
                    if resource.lower() not in dictionary:
                        dictionary[resource.lower()] = amount
                    else:
                        dictionary[resource.lower()] += amount
                    if resource.lower() == 'shards':
                        self.shards = dictionary[resource.lower()]
                        self.check_if_enough_materials_and_print(self.shards, self.fragments, self.motes,
                                                                 self.dict_data)
                    elif resource.lower() == 'motes':
                        self.motes = dictionary[resource.lower()]
                        self.check_if_enough_materials_and_print(self.shards, self.fragments, self.motes,
                                                                 self.dict_data)
                    elif resource.lower() == 'fragments':
                        self.fragments = dictionary[resource.lower()]
                        self.check_if_enough_materials_and_print(self.shards, self.fragments, self.motes,
                                                                 self.dict_data)
                    if self.flag:
                        return self.result

    def check_if_enough_materials_and_print(self, shards, fragments, motes, dictionary):
        if shards >= 250:
            self.legendary_item = 'Shadowmourne'
            self.result += f'{self.legendary_item} obtained!\n'
            self.flag = True
            self.shards = shards - 250
            self.dict_data['shards'] = self.shards
        elif fragments >= 250:
            self.legendary_item = 'Valanyr'
            self.result += f'{self.legendary_item} obtained!\n'
            self.flag = True
            self.fragments = fragments - 250
            self.dict_data['fragments'] = self.fragments
        elif motes >= 250:
            self.legendary_item = 'Dragonwrath'
            self.result += f'{self.legendary_item} obtained!\n'
            self.flag = True
            self.motes = motes - 250
            self.dict_data['motes'] = self.motes
        if self.flag:
            for material, amount in sorted(dictionary.items(), key=lambda x: (-x[1], x[0])):
                if material.lower() == 'shards':
                    self.result += f'{material.lower()}: {self.shards}\n'
                elif material.lower() == 'fragments':
                    self.result += f'{material.lower()}: {self.fragments}\n'
                elif material.lower() == 'motes':
                    self.result += f'{material.lower()}: {self.motes}\n'
            for material_junk, amount_junk in sorted(dictionary.items(), key=lambda x: x[0]):
                if material_junk.lower() != 'shards' and material_junk.lower() != 'fragments' and material_junk.lower() != 'motes':
                    self.result += f'{material_junk.lower()}: {amount_junk}\n'
            return self.result


one = Farming()