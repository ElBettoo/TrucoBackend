from jugador import Jugador
from moderador import Moderador
from defaultRole import DefaultRole
from usuarioRolesBehaviour import UsuarioRolesBehaviour

class Usuario(UsuarioRolesBehaviour):
    
    def __init__(self, username) -> None:
        self.username = username
        self.rol = DefaultRole()

    def set_role(self, rol):
        self.rol = rol

    def get_role(self):
        return self.rol.get_role()
    
    def set_jugador(self):
        self.rol = Jugador()


user = Usuario("prokki")

print(user.get_role())

user.set_role(Jugador())

user.rol.hola()

print(user.get_role())


user.set_role(Moderador())

print(user.get_role())
