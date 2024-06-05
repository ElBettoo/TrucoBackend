from Usuario.Usuario import Usuario

class UsersConnectedWrapper():
    def __init__(self) -> None:
        self.__connected_users = []
    
    @property
    def connected_users(self):
        return self.__connected_users

    def add_connected_user(self, sid, username):
        user_object = Usuario(sid, username)
        self.connected_users.append(user_object)
        
    def remove_connected_user(self, sid):
        for user in self.connected_users:
            if user.socket_id == sid:
                self.connected_users.remove(user)
                break

        print("NEW Connected users: ", self.connected_users)
        print("user: ", user)