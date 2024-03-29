from aiohttp import web
import socketio
import tracemalloc
import random

from Mazo import mazo 

sio = socketio.AsyncServer(cors_allowed_origins="*",)
app = web.Application()
sio.attach(app)

tracemalloc.start()

mazo = mazo.Mazo()


@sio.event
def connect(sid, environ):
    print("el socket:  ", sid, 'se conecto')

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

@sio.event
async def repartir_cartas(sid):
    
    player_cards = mazo.repartir_cartas([])
    
    await sio.emit('cartas_jugador', player_cards, to=sid)


if __name__ == '__main__':
    web.run_app(app)



