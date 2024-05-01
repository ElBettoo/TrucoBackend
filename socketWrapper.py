import asyncio
import aiohttp.web
import socketio
import tracemalloc
import random


class SocketIOApp:
    def __init__(self):
        self.sio = socketio.AsyncServer(cors_allowed_origins="*")
        self.app = aiohttp.web.Application()
        self.sio.attach(self.app)

        self.sio.on('connect', self.on_connect)
        self.sio.on('disconnect', self.on_disconnect)
        self.sio.on('repartir_cartas', self.repartir_cartas)
        self.sio.on('on_join_room', self.on_join_room)
        self.sio.on('ping', self.ping)
        
    async def on_connect(self, sid, environ):
        print("El socket:", sid, 'se conectó')

    async def on_disconnect(self, sid):
        print('Desconexión de', sid)

    async def repartir_cartas(self, sid, salaId):
        print("Manejando repartición de cartas!: ", sid)
        print("SID: ", sid)
        print("SalaID: ", salaId)
        await self.sio.emit('repartir_cartas', ['1', 'random.choice(100)', 'random.choice(1312412)'], to=salaId)

    
    async def on_join_room(self,sid,SalaId):
        print("Unido :3: " )
        print("S_room: ", sid)
        print("sala_room: ", SalaId)
        await self.sio.enter_room(sid, SalaId)
        await self.sio.emit("joined_room")

    async def ping(self,sid):
        print("ping from: ", sid)
        await self.sio.emit("ping")

    async def run(self):
        tracemalloc.start()
        runner = aiohttp.web.AppRunner(self.app)
        await runner.setup()
        site = aiohttp.web.TCPSite(runner, 'localhost', 8080)
        await site.start()

    

if __name__ == '__main__':
    socketio_app = SocketIOApp()
    asyncio.get_event_loop().run_until_complete(socketio_app.run())
    print("[SERVER] ON")
    asyncio.get_event_loop().run_forever()
