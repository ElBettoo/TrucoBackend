from abc import ABC, abstractmethod

class GameImplementation(ABC):
    def join_room(self, *args):
        raise NotImplementedError

    def start_game(self, *args):
        raise NotImplementedError

    def switch_room(self, *args):
        raise NotImplementedError
    
    def tirar_carta(self, *args):
        raise NotImplementedError

    def update_points(self, *args):
        raise NotImplementedError

