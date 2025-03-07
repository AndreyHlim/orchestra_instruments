from fastapi import FastAPI
from endpoints.generator import router_gen

import uvicorn

app = FastAPI()
app.include_router(router_gen, prefix='/generator')

if __name__ == '__main__':
    uvicorn.run(app='main:app', reload=True)
