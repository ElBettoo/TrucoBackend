from aiohttp import web
import socketio
import tracemalloc

sio = socketio.AsyncServer(cors_allowed_origins="*",)
app = web.Application()
sio.attach(app)
tracemalloc.start()


@sio.event
def connect(sid, environ):
    print("connect ", sid)

@sio.event
async def chat_message(sid, data):
    print("message ", data)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

@sio.event

def repartir_cartas(sid):
    print("anda")
    sio.emit('CartasJugador', [1,2,3])

if __name__ == '__main__':
    web.run_app(app)