from fastapi import APIRouter
from constants import DESCRIPTIONS, DEFAULT_SET_INSTR
from settings import SIGNAL_GEN_IP
import pyvisa

signal_gen = pyvisa.ResourceManager().open_resource(
    f'TCPIP0::{SIGNAL_GEN_IP}::inst0::INSTR'
)

router_gen = APIRouter()

@router_gen.post(
    '/',
    tags=['Настройки приборов'],
    summary='Настройка генератора ВЧ',
    description=DESCRIPTIONS['SETTING_DEVICE']
)
def gen_set(
        freq_ext: int = DEFAULT_SET_INSTR['SIGNAL_GEN']['REF_EXT'],
        mode: str = DEFAULT_SET_INSTR['SIGNAL_GEN']['MODE'],
        out_power: int = DEFAULT_SET_INSTR['SIGNAL_GEN']['OUT_LVL'],
    ):
    signal_gen.write(f':ROSCillator:EXTernal:FREQuency {freq_ext}')
    signal_gen.write(':ROSCillator:SOURce EXTernal')
    signal_gen.write(f':FREQuency:MODE {mode}')
    signal_gen.write(f':POWer:LEVel {out_power}')
    return 'Ok'

@router_gen.get(
    '/ser_num',
    tags=['Получение данных с генератора ВЧ'],
    summary='Узнать серийный номер генератора ВЧ (как проверка подключения)'
)
def gen_sernum() -> str:
    return signal_gen.query('*IDN?').split(',')[2]

@router_gen.get(
    '/rf_status',
    tags=['Получение данных с генератора ВЧ'],
    summary='Узнать включено ли излучение'
)
def gen_outrf() -> bool:
    return signal_gen.query(':OUTPut:STATe?').rstrip() == '1'

@router_gen.get(
    '/freq_center',
    tags=['Получение данных с генератора ВЧ'],
    summary='Узнать центральную частоту генератора [МГц]'
)
def gen_freqcentr() -> float:
    return float(signal_gen.query(':SOURce:FREQuency:CW?').rstrip())/1000000

@router_gen.get(
    '/freq_ref',
    tags=['Получение данных с генератора ВЧ'],
    summary='Узнать частоту внешнего опорного генератора [МГц]'
)
def gen_freqref() -> float:
    return float(signal_gen.query(':ROSCillator:EXTernal:FREQuency?').rstrip())/1000000

@router_gen.get(
    '/extref_status',
    tags=['Получение данных с генератора ВЧ'],
    summary='Узнать активирован ли вход внешнего опорного генератора'
)
def gen_refstatus() -> bool:
    return signal_gen.query(':ROSCillator:SOURce?') == 'EXT\n'

@router_gen.get(
    '/out_power',
    tags=['Получение данных с генератора ВЧ'],
    summary='Узнать установленную выходную мощность [dBm]'
)
def gen_outpwr() -> float:
    return float(signal_gen.query(':POWer:LEVel?').rstrip())

@router_gen.get(
    '/mode',
    tags=['Получение данных с генератора ВЧ'],
    summary='Узнать режим работы генератора'
)
def gen_mode() -> str:
    return signal_gen.query(':FREQuency:MODE?')

@router_gen.post(
    '/rf_on',
    tags=['Управление генератором ВЧ'],
    summary='Включить излучение'
)
def gen_rfon():
    signal_gen.write(':OUTPut:STATe ON')
    return 'Излучение включено'

@router_gen.post(
    '/rf_off',
    tags=['Управление генератором ВЧ'],
    summary='Выключить излучение'
)
def gen_rfoff():
    signal_gen.write(':OUTPut:STATe OFF')
    return 'Излучение выключено'

@router_gen.post(
    '/rf_freq',
    tags=['Управление генератором ВЧ'],
    summary='Установка частоты излучения [МГц]'
)
def gen_rffreq(frequence: float):
    signal_gen.write(f':SOURce:FREQuency:CW {frequence*1000000}')
    if gen_freqcentr() == frequence:
        return 'Ok'
    return 'Error'