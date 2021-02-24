class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player):
        if player in self.players:
            return f'Player {player.name} is already in the guild.'
        elif player.guild != 'Unaffiliated':
            return f'Player {player.name} is in another guild.'
        else:
            player.guild = self.name
            self.players.append(player)
            return f'Welcome player {player.name} to the guild {self.name}'

    def kick_player(self, player_name):
        for player_object in self.players:
            if player_object.name == player_name:
                self.players.remove(player_object)
                return f'Player {player_name} has been removed from the guild.'
        return f'Player {player_name} is not in the guild.'

    def guild_info(self):
        data = f'Guild {self.name}\n'
        data_1 = ''
        for player_object in self.players:
            data_1 += player_object.player_info()
        result = data + data_1
        return result
