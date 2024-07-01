
class SocketsConnectedWrapper():
    def __init__(self) -> None:
        self.__connected_sockets = []

    @property
    def connected_sockets(self):
        return self.__connected_sockets
    
    def add_user_socket(self, user_socket):
        self.connected_sockets.append(user_socket)
        
    def get_user_socket_by_socket_id(self, sid):
        for user_socket in self.connected_sockets:
            if user_socket.socket_id == sid:
                return user_socket

    def remove_user_socket(self, sid):
        for user_socket in self.connected_sockets:
            if user_socket.socket_id == sid:
                self.connected_sockets.remove(user_socket)
                break  