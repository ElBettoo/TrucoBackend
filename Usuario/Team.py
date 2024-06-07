class Team:
    def __init__(self, id, name="Unnamed") -> None:
        self.__id = id
        self.__name = name
        self.__points = 0
        self.__players = []

    def add_player(self, new_player):
        self.players.append(new_player)

    def remove_player(self, old_player):
        self.players.remove(old_player)

    @property
    def id(self):
        return self.__id
    
    @property
    def name(self):
        return self.__name
    
    @property
    def points(self):
        return self.__points
    @points.setter
    def points(self, pointis):
        self.__points = pointis 
    
    @property
    def players(self):
        return self.__players
    

    
