class UserSocket:
    def __init__(self, socket_id) -> None:
        self.__socket_id = socket_id

    @property
    def socket_id(self):
        return self.__socket_id
    