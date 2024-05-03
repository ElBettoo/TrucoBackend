import asyncio
import aiohttp.web
import socketio
import tracemalloc

from Sala.Sala import Sala as SalaClass
from Usuario.Usuario import Usuario


class SocketIOApp:
    def __init__(self):

        self.active_rooms = []
        
        self.sio = socketio.AsyncServer(cors_allowed_origins="*")
        self.app = aiohttp.web.Application()
        self.sio.attach(self.app)

        
        self.sio.on('connect', self.on_connect)
        self.sio.on('disconnect', self.on_disconnect)
        self.sio.on('repartir_cartas', self.repartir_cartas)
        self.sio.on('join_room', self.on_join_room)
        self.sio.on('ping', self.ping)
    
    def get_active_rooms(self):
        return self.active_rooms

    def get_sala(self, SalaId):
        for sala_i in self.get_active_rooms():
            if sala_i.get_sala_code() == SalaId:
                return sala_i

        nueva_sala = SalaClass(SalaId)
        self.add_active_room(nueva_sala)
        return nueva_sala
                
    def add_active_room(self,sala)-> SalaClass:
        self.active_rooms.append(sala)


    async def on_connect(self, sid, environ):
        print("El socket:", sid, 'se conectó')

    async def on_disconnect(self, sid):
        print('Desconexión de', sid)

    async def repartir_cartas(self, sid, salaId):
      #  print("Manejando repartición de cartas!: ", sid)
      #  print("SID: ", sid)
       # print("SalaID: ", salaId)
        await self.sio.emit('repartir_cartas', ['1', 'random.choice(100)', 'random.choice(1312412)'], to=salaId)

    async def on_join_room(self,sid,SalaId,Username):
        print("El usuario: ", Username, "se unio a la sala: ", SalaId)


        current_sala = self.get_sala(SalaId)
        current_user = Usuario(sid, Username)
        current_sala.add_user(current_user)

        print("Usuarios de la sala: ", current_sala.get_users())
        print("Salas totalesa: ", self.active_rooms)

        await self.sio.enter_room(sid, SalaId)
        await self.sio.emit("joined_room")

        print('Sala actual tiene:', len(current_sala.get_users()), 'usuarios')

        if len(current_sala.get_users()) >= 2:
            print("esta caca anda")
            await self.sio.emit('recibir_jugadores', current_sala.get_usernames(), to=SalaId)

    async def ping(self,sid):
        print("ping from: ", sid)
        await self.sio.emit("ping")

    async def run(self):
        tracemalloc.start()
        runner = aiohttp.web.AppRunner(self.app)
        await runner.setup()
        site = aiohttp.web.TCPSite(runner, 'localhost', 8080)
        await site.start()


    
    
def run_game(socketApp):
    asyncio.get_event_loop().run_until_complete(socketApp.run())
    print("[SERVER] ON")
    asyncio.get_event_loop().run_forever()
    pass

if __name__ == '__main__':
    socketio_app = SocketIOApp()
    run_game(socketio_app)