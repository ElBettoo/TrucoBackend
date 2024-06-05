from Sala.Sala import Sala as Sala
class SalaWrapper():
    def __init__(self) -> None:
        self.__active_rooms = []


    def get_room_by_sid(self, sid): # Los juguetes lo ven todo
        for sala in self.active_rooms:
            for usuario in sala.users:
                if usuario.socket_id == sid:
                    return sala
                
    def get_sala(self, SalaId):
        existing_room = self.__add_to_existing_room(SalaId)

        if existing_room:
            return existing_room
        else: 
            return self.__create_new_room(SalaId)

    #Getters
    @property
    def active_rooms(self):
        return self.__active_rooms

    #Private Methods    
    def __add_active_room(self,sala)-> Sala:
        self.active_rooms.append(sala)
 
    def __add_to_existing_room(self, SalaId):
        for sala_i in self.active_rooms:
            if sala_i.codigo_sala == SalaId:
                return sala_i
        return None
    
    def __create_new_room(self, SalaId):
        nueva_sala = Sala(SalaId)
        self.__add_active_room(nueva_sala)
        return nueva_sala