import endpoints.connection as connect
from constants import DEFAULT_SET_SIGNAL
from fastapi import APIRouter

router_gen = APIRouter()


@router_gen.post(
    '/',
    tags=['Настройки приборов'],
    summary='Настройка генератора ВЧ',
)
def gen_set(
        freq_ext: int = DEFAULT_SET_SIGNAL['REF_EXT'],
        mode: str = DEFAULT_SET_SIGNAL['MODE'],
        out_power: int = DEFAULT_SET_SIGNAL['OUT_LVL'],
):
    connect.signal_gen.write(f':ROSCillator:EXTernal:FREQuency {freq_ext}')
    connect.signal_gen.write(':ROSCillator:SOURce EXTernal')
    connect.signal_gen.write(f':FREQuency:MODE {mode}')
    connect.signal_gen.write(f':POWer:LEVel {out_power}')
    return 'Ok'


@router_gen.get(
    '/ser_num',
    tags=['Получение данных с генератора ВЧ'],
    summary='Узнать серийный номер генератора ВЧ (как проверка подключения)'
)
def gen_sernum() -> str:
    """Извлекает серийный номер, записанный во внутренней памяти генератора."""
    return connect.signal_gen.query('*IDN?').split(',')[2]


@router_gen.get(
    '/rf_status',
    tags=['Получение данных с генератора ВЧ'],
    summary='Узнать включено ли излучение'
)
def gen_outrf() -> bool:
    """Состояние высокочастотного выхода генератора: вкл или выкл."""
    return connect.signal_gen.query(':OUTPut:STATe?').rstrip() == '1'


@router_gen.get(
    '/freq_center',
    tags=['Получение данных с генератора ВЧ'],
    summary='Узнать центральную частоту генератора [МГц]'
)
def gen_freqcentr() -> float:
    """Установленная частота генератора."""
    return float(connect.signal_gen.query(
        ':SOURce:FREQuency:CW?'
    ).rstrip())/1000000


@router_gen.get(
    '/freq_ref',
    tags=['Получение данных с генератора ВЧ'],
    summary='Узнать частоту внешнего опорного генератора [МГц]'
)
def gen_freqref() -> float:
    """Ожидаемая частота внешнего опорного генератора."""
    return float(connect.signal_gen.query(
        ':ROSCillator:EXTernal:FREQuency?'
    ).rstrip())/1000000


@router_gen.get(
    '/extref_status',
    tags=['Получение данных с генератора ВЧ'],
    summary='Узнать активирован ли вход внешнего опорного генератора'
)
def gen_refstatus() -> bool:
    """Состояние выхода внешнего опорного генератора."""
    return connect.signal_gen.query(':ROSCillator:SOURce?') == 'EXT\n'


@router_gen.get(
    '/out_power',
    tags=['Получение данных с генератора ВЧ'],
    summary='Узнать установленную выходную мощность [dBm]'
)
def gen_outpwr() -> float:
    """Уровень генерации на выходе RF генератора."""
    return float(connect.signal_gen.query(':POWer:LEVel?').rstrip())


@router_gen.get(
    '/mode',
    tags=['Получение данных с генератора ВЧ'],
    summary='Узнать режим работы генератора'
)
def gen_mode() -> str:
    """Режим работы генератора"""
    return connect.signal_gen.query(':FREQuency:MODE?')


@router_gen.post(
    '/rf_on',
    tags=['Управление генератором ВЧ'],
    summary='Включить излучение'
)
def gen_rfon():
    """Активация выхода RF генератора."""
    connect.signal_gen.write(':OUTPut:STATe ON')
    return 'Излучение включено'


@router_gen.post(
    '/rf_off',
    tags=['Управление генератором ВЧ'],
    summary='Выключить излучение'
)
def gen_rfoff():
    """Деактивация выхода RF генератора."""
    connect.signal_gen.write(':OUTPut:STATe OFF')
    return 'Излучение выключено'


@router_gen.post(
    '/rf_freq',
    tags=['Управление генератором ВЧ'],
    summary='Установка частоты излучения [МГц]'
)
def gen_rffreq(frequence: float):
    connect.signal_gen.write(f':SOURce:FREQuency:CW {frequence*1000000}')
    return gen_freqcentr() == frequence
