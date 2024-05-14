class Usuario:
    def __init__(self, socket_id, username) -> None:
        self.__username = username
        self.__socket_id = socket_id
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
        return self.__socket_id