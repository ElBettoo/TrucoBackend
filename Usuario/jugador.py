from mano import Mano
from usuarioRolesBehaviour import UsuarioRolesBehaviour

class Jugador(UsuarioRolesBehaviour):
    def __init__(self) -> None:
        self.mano = Mano()
    
    def get_role(self):
        return "JUGADOR"
    

    def hola(self):
        print("HOLIII")