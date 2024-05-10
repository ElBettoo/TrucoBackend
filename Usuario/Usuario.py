class Usuario:
    def __init__(self, socketId, username ) -> None:
        self.username = username
        self.socketId = socketId
        self.points = 0
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
        return self.socketId