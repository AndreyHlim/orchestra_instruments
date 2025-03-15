from typing import Annotated

import pyvisa
from fastapi import APIRouter, Depends

from schemas.connections import SInstumentsAdd, TypeInstr
from schemas.generators import SGeneratorsAdd

router_connect = APIRouter()
router_disconnect = APIRouter()
instruments = {
    'Generator Signals': None,
    'Generator Sounds': None,
    'Spectrum Analyzer': None,
}


@router_connect.get(
    '/all',
    summary='Получение списка подключенных приборов'
)
def get_instruments():
    return {'Подключенные приборы': instruments}


@router_connect.post(
    '/instruments',
    summary='Подключение к прибору по IP-адресу'
)
def gen_rf(genrf: Annotated[SInstumentsAdd, Depends()]):
    global signal_gen
    signal_gen = connection_instrument(genrf)
    return instruments


def connection_instrument(genrf: SInstumentsAdd):
    instr = pyvisa.ResourceManager().open_resource(
        f'TCPIP0::{genrf.ip_address}::inst0::INSTR'
    )
    if genrf.type_instrument == TypeInstr.generator_signals:
        instr = SGeneratorsAdd(
            ip_address=genrf.ip_address,
            type_instrument=genrf.type_instrument,
            ser_num=instr.resource_info[3],
            model=instr.resource_info[2],
        )
    else:
        instr = None
    instruments[genrf.type_instrument] = instr
    return instr


@router_disconnect.post(
    '/generator',
    summary='Отключение от прибора',
)
def disconnect_instr(type_instr: TypeInstr):
    if instruments[type_instr] is not None:
        instr = instruments[type_instr]
        instr.close()
        return f'Подключение с {type_instr} разорвано'
    return f'Поделючение с {type_instr} отсутствовало'
