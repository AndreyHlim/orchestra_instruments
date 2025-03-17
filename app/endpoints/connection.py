from typing import Annotated

import pyvisa
from fastapi import APIRouter, Depends

from schemas.connections import SInstrInfo, SInstrumentsAdd, TypeInstr
from schemas.generators import SGeneratorAdd
from schemas.instruments import Instruments
from schemas.sounds import SSoundGenAdd

router_connect = APIRouter()
router_disconnect = APIRouter()
instruments = Instruments(
    signal_generator=None,
    sound_generator=None,
    spectrum_analizer=None,
)


@router_connect.get(
    '/all',
    summary='Получение списка подключенных приборов'
)
def get_instruments() -> Instruments:
    return instruments


@router_connect.post(
    '/instruments',
    summary='Подключение к прибору по IP-адресу'
)
def instr_connect(genrf: Annotated[SInstrumentsAdd, Depends()]) -> SInstrInfo:
    global signal_gen
    signal_gen = connection_instrument(genrf)
    return getattr(instruments, genrf.type_instrument.name)


def connection_instrument(genrf: SInstrumentsAdd):
    instr = pyvisa.ResourceManager().open_resource(
        f'TCPIP0::{genrf.ip_address}::inst0::INSTR'
    )
    if genrf.type_instrument == TypeInstr.signal_generator:
        instrument = SGeneratorAdd(
            ip_address=genrf.ip_address,
            type_instrument=genrf.type_instrument,
            model=instr.resource_info[2],
            ser_num=instr.resource_info[3],
        )
        instruments.signal_generator = instrument
    elif genrf.type_instrument == TypeInstr.sound_generator:
        instrument = SSoundGenAdd(
            ip_address=genrf.ip_address,
            type_instrument=genrf.type_instrument,
            model=instr.resource_info[2],
            ser_num=instr.resource_info[3],
        )
        instruments.sound_generator = instrument
    else:
        instr = None
    return instr


@router_disconnect.post(
    '/generator',
    summary='Отключение от прибора',
)
def disconnect_instr(type_instr: TypeInstr) -> str:
    instr = getattr(instruments, type_instr.name)
    if  instr is not None:
        pyvisa.ResourceManager().open_resource(
            f'TCPIP0::{instr.ip_address}::inst0::INSTR'
        ).close()
        # Обновить instruments поставив None в нужном месте
        return f'Подключение с {type_instr} разорвано.'
    return f'Подключение с {type_instr} отсутствовало.'
