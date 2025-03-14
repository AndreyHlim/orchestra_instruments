from typing import Annotated

import pyvisa
from fastapi import APIRouter, Depends
from schemas.connections import SInstumentsAdd, TypeInstr
from schemas.generators import SGeneratorsAdd

router_connect = APIRouter()
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
    summary='Подключение к высокочастотному генератору'
)
def gen_rf(genrf: Annotated[SInstumentsAdd, Depends()]):
    global signal_gen
    signal_gen = connection_instrument(genrf.ip_address, genrf.type_instrument)
    return instruments


def connection_instrument(ip_address: str, type_instr: TypeInstr):
    instr = pyvisa.ResourceManager().open_resource(
        f'TCPIP0::{ip_address}::inst0::INSTR'
    )
    if type_instr == TypeInstr.generator_signals:
        instr = SGeneratorsAdd(
            ip_address=ip_address,
            type_instrument=type_instr,
            ser_num='11111111',
            model='model1111',
        )
    else:
        instr = None
    instruments[type_instr] = instr.resource_info
    instruments[type_instr] = instr
    return instr
