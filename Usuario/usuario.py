from .jugador import Jugador
#from moderador import Moderador
from .defaultRole import DefaultRole
#from usuarioRolesBehaviour import UsuarioRolesBehaviour
import inspect

class Usuario():
    
    def __init__(self, username) -> None:
        self.username = username
        self.rol = DefaultRole()

    def set_role(self, rol):
        self.rol = rol

    def get_role(self):
        return self.rol
    
    def set_jugador(self):
        self.rol = Jugador()

    def perform_hola(self):
        try:
            self.get_role().hola()
        except:
            current_function = inspect.currentframe().f_code.co_name
            print(f"{self.get_role()}: doesn't support {current_function}: ")

    def perform_get_mano(self):
        try:
           # print(self.get_role())
            return self.get_role().get_mano().get_cards()
        except:
            current_function = inspect.currentframe().f_code.co_name
            print(f"{self.get_role()}: doesn't support {current_function}: ")

    def obtener_cartas(self, cartas):
        try:
            return self.get_role().get_mano().set_cards(cartas)
        except:
            current_function = inspect.currentframe().f_code.co_name
            print(f"{self.get_role()}: doesn't support {current_function}: ")

    def perform_tirar_carta(self, card_index):
        return self.get_role().tirar_carta(card_index)
       

    

