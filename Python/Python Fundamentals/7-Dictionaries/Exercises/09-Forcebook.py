class ForceUsers:
    def __init__(self):
        self.jedi = {}
        self.final_dict = {}
        self.command_split_1_dash = None
        self.command_split_2_arrow = None
        self.filling_the_dict()

    def filling_the_dict(self):
        while True:
            command = input()
            if command == 'Lumpawaroo':
                self.print_output()
                break
            if '|' in command:
                self.command_split_1_dash = command.split(' | ')
                self.check_if_force_user_exist()
            elif ' -> ' in command:
                self.command_split_2_arrow = command.split(' -> ')
                self.change_side_if_exist_if_not_add()
        return

    def check_if_force_user_exist(self):
        side = self.command_split_1_dash[0]
        name = self.command_split_1_dash[1]
        user_in_dict = False
        token_1 = False
        token_2 = False
        if side not in self.jedi:
            token_1 = True
        if len(self.jedi.values()) == 0:
            token_2 = True
        for item in self.jedi.values():
            if name not in item and name != item:
                token_2 = True
        if token_1 == True and token_2 == True:
            self.jedi[side] = [name]
        else:
            for users in self.jedi.values():
                if name in users:
                    user_in_dict = True
                    break
            if not user_in_dict:
                self.jedi[side].append(name)
        return

    def change_side_if_exist_if_not_add(self):
        name = self.command_split_2_arrow[0]
        side = self.command_split_2_arrow[1]
        if side not in self.jedi:
            for list_iteration in self.jedi.values():
                if name in list_iteration:
                    list_iteration.remove(name)
                elif name == list_iteration:
                    self.jedi.clear()
            self.jedi[side] = [name]
            print(f'{name} joins the {side} side!')
        else:
            for key, users in self.jedi.items():
                if name in users:
                    continue
                else:
                    for jedi in self.jedi.values():
                        if name in jedi:
                            jedi.remove(name)
                    self.jedi[side].append(name)
                    print(f'{name} joins the {side} side!')
                break


    def print_output(self):
        self.final_dict = self.jedi.copy()
        for side in self.jedi:
            if len(self.jedi[side]) == 0:
                self.final_dict.pop(side)

        for force_side, force_users_count in sorted(self.final_dict.items(), key=lambda x: (-len(x[1]), x[0].lower())):
            print(f'Side: {force_side}, Members: {len(force_users_count)}')
            for user in sorted(force_users_count, key=lambda x: x.lower()):
                print(f'! {user}')


batch_1 = ForceUsers()