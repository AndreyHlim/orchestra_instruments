from fastapi import FastAPI
from endpoints.generator import router_gen
from endpoints.connection import router_connect
import uvicorn


app = FastAPI()
app.include_router(router_connect, prefix='/connections',tags=['Подключение с приборами'],)
app.include_router(router_gen, prefix='/generators')


if __name__ == '__main__':
    uvicorn.run(app='main:app', reload=True)
