import aiohttp.web
import socketio
import tracemalloc
from Sala.Sala import Sala as Sala
from Usuario.Usuario import Usuario

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
    

class SocketsConnectedWrapper():
    def __init__(self) -> None:
        self.__connected_sockets = []

    @property
    def connected_sockets(self):
        return self.__connected_sockets
    
    def add_user_socket(self, user):
        self.connected_sockets.append(user)

    def get_user_socket_by_socket_id(self, sid):
        for user_socket in self.connected_sockets:
            if user_socket.socket_id == sid:
                return user_socket

    def remove_user_socket(self, sid):
        for user_socket in self.connected_sockets:
            if user_socket.socket_id == sid:
                self.connected_sockets.remove(user_socket)
                break  
   
class UsersConnectedWrapper():
    def __init__(self) -> None:
        self.__connected_users = []
    
    @property
    def connected_users(self):
        return self.__connected_users

    def add_connected_user(self, sid, username):
        user_object = Usuario(sid, username)
        self.connected_users.append(user_object)
        
    def remove_connected_user(self, sid):
        for user in self.connected_users:
            if user.socket_id == sid:
                self.connected_users.remove(user)
                break

        print("NEW Connected users: ", self.connected_users)
        print("user: ", user)
        

                
class SocketIOApp:
    def __init__(self):

        self.__sala_wrapper = SalaWrapper()
        self.__sockets_connected_wrapper = SocketsConnectedWrapper()
        self.__users_connected_wrapper = UsersConnectedWrapper()
        self.sio = socketio.AsyncServer(cors_allowed_origins="*")
        self.app = aiohttp.web.Application()
        self.sio.attach(self.app)

    @property
    def sala_wrapper(self):
        return self.__sala_wrapper
    
    @property
    def sockets_connected_wrapper(self):
        return self.__sockets_connected_wrapper
    
    @property
    def users_connected_wrapper(self):
        return self.__users_connected_wrapper

    async def run(self):
        tracemalloc.start()
        runner = aiohttp.web.AppRunner(self.app)
        await runner.setup()
        site = aiohttp.web.TCPSite(runner, 'localhost', 8080)
        await site.start()

    def on_event(self, *args):
        self.sio.on(*args)

    async def emit(self, *args):
        await self.sio.emit(*args)
    
    async def emit_to_sala(self, salaId, *args):
        event = args[0]
        event_data = []

        for x in args:
            if x == event:
                continue
            
            event_data.append(x)

        await self.sio.emit(to=salaId, event=event, data=event_data)
    
    async def emit_to_player(self, socketId, *args):
        event = args[0]
        event_data = []

        for x in args:
            if x == event:
                continue
            
            event_data.append(x)

        await self.sio.emit(to=socketId, event=event, data=event_data)

WRAPPER = SocketIOApp()