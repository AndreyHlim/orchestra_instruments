import uvicorn
from fastapi import FastAPI

from endpoints.connection import router_connect, router_disconnect
from endpoints.generator import router_gen

app = FastAPI()
app.include_router(
    router_connect,
    prefix='/connections',
    tags=['Подключение с приборами'],
)
app.include_router(
    router_disconnect,
    prefix='/disconnect',
    tags=['Подключение с приборами'],
)
app.include_router(router_gen, prefix='/generators')


if __name__ == '__main__':
    uvicorn.run(app='main:app', reload=True)
