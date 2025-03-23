import uvicorn
from fastapi import FastAPI
from routers import router_v1


app = FastAPI()

app.include_router(router_v1, prefix='/api_v1')

if __name__ == '__main__':
    uvicorn.run(app='main:app', reload=True)
