
class SocketsConnectedWrapper():
    def __init__(self) -> None:
        print("ME LO RESETEARON TODO CARMAIN, Y ESO ERA HOY")
        self.__connected_sockets = []

    @property
    def connected_sockets(self):
        return self.__connected_sockets
    
    def add_user_socket(self, user_socket):
        print("asdasdsa djsakl; ", user_socket)
        self.connected_sockets.append(user_socket)
        print(self.connected_sockets)

    def get_user_socket_by_socket_id(self, sid):
        print("BUENA PORKY MATATE", self.connected_sockets)
        for user_socket in self.connected_sockets:
            if user_socket.socket_id == sid:
                return user_socket

    def remove_user_socket(self, sid):
        print("ME LO REMOVEARON TODO CARMAIN, Y ESO ERA HOY")
        for user_socket in self.connected_sockets:
            if user_socket.socket_id == sid:
                self.connected_sockets.remove(user_socket)
                break  