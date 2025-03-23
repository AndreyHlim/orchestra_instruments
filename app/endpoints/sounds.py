from endpoints.connection import get_instr
from fastapi import APIRouter

router_sound = APIRouter()


@router_sound.get(
    '/ser_num',
    tags=['Получение данных с генератора НЧ'],
    summary='Узнать серийный номер генератора НЧ'
)
def gen_sernum() -> str:
    """Извлекает серийный номер, записанный во внутренней памяти генератора."""
    return get_instr('sound_generator').query('*IDN?')
