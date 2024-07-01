from .GameImplementations import GameImplementation

class ConsoleImplementation(GameImplementation):
    def join_room(self,*args):
        print("Porky joined room")
        return "Porky joined room"