class UserSocket:
    def __init__(self, socket_id) -> None:
        self.__socket_id = socket_id
        self.__user = None

    @property
    def socket_id(self):
        return self.__socket_id
    
    def assign_user(self, User):
        self.__user = User

    @property
    def user(self):
        return self.__user
    