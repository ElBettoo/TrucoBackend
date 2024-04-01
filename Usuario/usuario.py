from .jugador import Jugador
from .moderador import Moderador
from .defaultRole import DefaultRole
from .usuarioRolesBehaviour import UsuarioRolesBehaviour

class Usuario(UsuarioRolesBehaviour):
    
    def __init__(self, username) -> None:
        self.username = username
        self.rol = DefaultRole()
        self.__rolesPosibles = [DefaultRole, Jugador, Moderador]

    def set_role(self, rol):
        print(rol, rol in self.__rolesPosibles)
        self.rol = rol

    def get_role(self):
        return self.rol.get_role()
    
    def set_jugador(self):
        self.rol = Jugador()