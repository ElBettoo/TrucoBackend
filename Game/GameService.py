from Usuario.Usuario import Usuario
from Mazo.Mazo import Mazo
from Usuario.UserSocket import UserSocket
from .UserHandler import UserHandler
from Network.socketWrapper import WRAPPER

class GameService:
    def __init__(self, game_implementation) -> None:
        self.__game_implementation = game_implementation
    
    @property
    def game_implementation(self):
        return self.__game_implementation

    def join_room(self,*args):
        return self.game_implementation.join_room(args)
        
    def start_game(self, *args):
        return self.game_implementation.start_game(args)
            
    def switch_round(self,*args):
        print("args de la puta sala: ", args)
        return self.game_implementation.switch_round(*args) #SI NO PONGO EL ASTERISCO SE ROMPE
    
    def tirar_carta(self,*args):
        return self.game_implementation.tirar_carta(args)

    def leave_room(self,*args):
        self.game_implementation.leave_room(args)

    def update_points(self, *args):
        return self.game_implementation.update_points(args)

    def add_user_socket(self, *args):
        print("ARGUMENTOS TOIET: ", args)
        return self.game_implementation.add_user_socket(args)