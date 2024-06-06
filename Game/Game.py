from Usuario.Usuario import Usuario
from Mazo.Mazo import Mazo
from Usuario.UserSocket import UserSocket
from .UserHandler import UserHandler
from Network.socketWrapper import WRAPPER


class Game:
    def __init__(self, user_handler) -> None:
        self.__user_handler = user_handler
        self.__socket = WRAPPER

    def join_room(self, sid,SalaId,Username):
        current_sala = self.socket.sala_wrapper.get_sala(SalaId)
        user_socket = self.socket.sockets_connected_wrapper.get_user_socket_by_socket_id(sid)
        
        self.socket.users_connected_wrapper.add_connected_user(user_socket, Username) # Esto no existia y no podias ver los usuarios conectados :V


        new_user = self.user_handler.create_user(name=Username, user_socket=user_socket)

        user_socket.assign_user(new_user)
        current_sala.add_user(new_user)
    
        return {"current_sala": current_sala}
        
    
    @property
    def socket(self):
        return self.__socket
    @property
    def user_handler(self):
        return self.__user_handler