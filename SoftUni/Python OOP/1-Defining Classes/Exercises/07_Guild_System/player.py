class Player:
    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = int(hp)
        self.mp = mp
        self.skills = {}
        self.guild = 'Unaffiliated'

    def add_skill(self, skill_name, mana_cost):
        if skill_name not in self.skills:
            self.skills[skill_name] = mana_cost
            return f'Skill {skill_name} added to the collection of the player {self.name}'
        return 'Skill already added'

    def player_info(self):
        data_1 = f'Name: {self.name}\n' \
               f'Guild: {self.guild}\n' \
               f'HP: {self.hp}\n' \
               f'MP: {self.mp}\n'

        data_2 = ''
        for skill_name, mp_cost in self.skills.items():
            data_2 += f'==={skill_name} - {mp_cost}\n'
        result = data_1 + data_2
        return result
