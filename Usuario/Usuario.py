class Usuario:
    def __init__(self, user_socket, username="juanitrox") -> None:
        self.__username = username
        self.__user_socket = user_socket
        self.__team = None
        self.mano = None
        
        
        
    def set_mano(self, nueva_mano):
        self.mano = nueva_mano

    def get_mano(self):
        mano = self.mano.cartas
        mano_serialized = []
        for carta in mano:
            mano_serialized.append(carta.key)
        return mano_serialized
    
    
    def get_socket_id(self):
        return self.socket_id
    
    def tirar_carta(self, carta_tirada):
        self.get_mano.remove_card(carta_tirada)
        

    @property
    def team(self):
        return self.__team
    
    @team.setter
    def team(self, new_team):
        self.__team = new_team

    @property
    def username(self):
        return self.__username
    
    @property
    def socket_id(self):
        return self.__user_socket.socket_id