class Usuario:
    def __init__(self, socketId, username ) -> None:
        self.username = username
        self.socketId = socketId
        self.points = 0
        