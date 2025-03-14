import pyvisa
from enum import Enum
from fastapi import APIRouter, Depends
from schemas.connections import SInstumentsAdd
from typing import Annotated


router_connect = APIRouter()
instruments = {
    'Generator Signals': None,
    'Generator Sounds': None,
    'Spectrum Analyzer': None,
}

class TypeInstr(str, Enum):
    generator_signals = 'Generator Signals'
    generator_sounds = 'Generator Sounds'
    spectrum_analyzer = 'Spectrum Analyzer'


@router_connect.get(
    '/all',
    summary='Получение списка подключенных приборов'
)
def get_instruments():
    return {'Подключенные приборы': instruments}


@router_connect.post(
    '/generator',
    summary='Подключение к высокочастотному генератору'
)
def gen_rf(genrf: Annotated[SInstumentsAdd, Depends()], inst_type: TypeInstr):
    global signal_gen
    signal_gen=connection_instrument(genrf.ip_address, inst_type)
    return instruments


# @router_connect.post(
#     '/sound',
#     summary='Подключение к генератору низких частот'
# )
# def gen_lf(genlf: Annotated[SInstumentsAdd, Depends()]):
#     global sound_gen
#     sound_gen=connection_instrument(genlf.ip_address,'Generator Sounds')
#     return instruments


# @router_connect.post(
#     '/analizer',
#     summary='Подключение к анализатору спектра'
# )
# def analizer(analizer: Annotated[SInstumentsAdd, Depends()]):
#     global spectrum_analizer
#     spectrum_analizer=connection_instrument(analizer.ip_address,'Spectrum Analyzer')
#     return instruments


def connection_instrument(ip_address: str, type_instr: TypeInstr):
    instr = pyvisa.ResourceManager().open_resource(
        f'TCPIP0::{ip_address}::inst0::INSTR'
    )
    instruments[type_instr] = instr.resource_info
    return instr