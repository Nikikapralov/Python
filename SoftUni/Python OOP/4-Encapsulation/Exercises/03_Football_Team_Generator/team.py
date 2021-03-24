class Team:
    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
        self.__players = []

    def __check_if_already_in(self, player):
        if player in self.__players:
            return True
        else:
            return False

    def __get_player(self, player_name):
        player = [p for p in self.__players if p.name == player_name]
        if len(player) > 0:
            return player[0]
        else:
            return False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        self.__rating = value

    @property
    def players(self):
        return self.__players

    @players.setter
    def players(self, value):
        self.__players = value

    def add_player(self, player):
        if self.__check_if_already_in(player):
            return f'Player {player.name} has already joined'
        self.__players.append(player)
        return f'Player {player.name} joined team {self.__name}'

    def remove_player(self, player_name):
        player = self.__get_player(player_name)
        if not player:
            return f'Player {player_name} not found'
        self.__players.remove(player)
        return player

