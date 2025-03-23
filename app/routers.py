from fastapi import APIRouter

from endpoints.connection import router_connect, router_disconnect
from endpoints.generator import router_gen
from endpoints.sounds import router_sound


router_v1 = APIRouter()
router_v1.include_router(
    router_connect,
    prefix='/connections',
    tags=['Подключение с приборами'],
)
router_v1.include_router(
    router_disconnect,
    prefix='/disconnections',
    tags=['Подключение с приборами'],
)
router_v1.include_router(router_gen, prefix='/generators')
router_v1.include_router(router_sound, prefix='/sounds')
