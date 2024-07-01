from Usuario.Usuario import Usuario

class UsersConnectedWrapper():
    def __init__(self) -> None:
        self.__connected_users = []
    
    @property
    def connected_users(self):
        return self.__connected_users

    def add_connected_user(self, user_socket, username):

        user_object = Usuario(user_socket, username)
        user_socket.assign_user(user_object)
        self.connected_users.append(user_object)

        return user_object #PORQUE NO RETORNEABA ESTO ?
        
    def remove_connected_user(self, sid):
        for user in self.connected_users:
            if user.socket_id == sid:
                self.connected_users.remove(user)
                break
