from Usuario.Usuario import Usuario

class UserHandler:
    def __init__(self) -> None:
        pass

    def create_user(self, name, user_socket):
        new_user = Usuario(user_socket, name)

        return new_user 