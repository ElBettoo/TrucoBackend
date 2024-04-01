from .mano import Mano
from .usuarioRolesBehaviour import UsuarioRolesBehaviour

class Jugador(UsuarioRolesBehaviour):
    def __init__(self) -> None:
        self.mano = Mano()
        self.num_equipo = None
    
    def get_mano(self):
        return self.mano

    def get_nombre_role(self):
        return "JUGADOR"
    
    def hola(self):
        print("HOli ")

    def tirar_carta(self, card_index):
        return(self.get_mano().get_one_card(card_index))

    def set_num_equipo(self, num_equipo):
        self.num_equipo = num_equipo
    
    def get_num_equipo(self):
        return self.num_equipo