class Usuario:
    def __init__(self, socketId, username ) -> None:
        self.username = username
        self.socketId = socketId
        self.points = 0
        self.mano = None
        
    def set_mano(self, nueva_mano):
        self.mano = nueva_mano