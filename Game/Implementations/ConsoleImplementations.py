from .GameImplementations import GameImplementation

class ConsoleImplementation(GameImplementation):
    def join_room(self,*args):
        
        sala = []
        
        sala.append("porky")

        print("Porky joined room")
        return "Porky joined room"