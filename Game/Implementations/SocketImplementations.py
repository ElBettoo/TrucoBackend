from .GameImplementations import GameImplementation



class SocketImplementation(GameImplementation):
    def __init__(self, socket, sala_wrapper, sockets_connected_wrapper) -> None:
        
        self.__socket = socket
        self.__sala_wrapper = sala_wrapper
        self.__sockets_connected_wrapper = sockets_connected_wrapper

    def join_room(self, *args): 
        
        sid, SalaId, Username = args[0]
        current_sala = self.sala_wrapper.get_sala(SalaId)      
        user_socket = self.sockets_connected_wrapper.get_user_socket_by_socket_id(sid) #vamos a asumir por ahora que lo unico qe se puede conectar es un user_socket, nada de interfaces ni boludeces        
        new_user = self.socket.users_connected_wrapper.add_connected_user(user_socket, Username) #Esto no existia y no podias ver los usuarios conectados :V
        current_sala.add_user(new_user)
        
        return {"current_sala": current_sala}

    @property
    def sockets_connected_wrapper(self):
        return self.__sockets_connected_wrapper 
    
    @property
    def sockets_connected_wrapper(self):
        return self.__sockets_connected_wrapper

    @property
    def socket(self):
        return self.__socket

    @property
    def sala_wrapper(self):
        return self.__sala_wrapper