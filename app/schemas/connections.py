from enum import Enum

from pydantic import BaseModel, IPvAnyAddress


class TypeInstr(str, Enum):
    signal_generator = 'Generator Signals'
    sound_generator = 'Generator Sounds'
    spectrum_analizer = 'Spectrum Analyzer'


class SInstrumentsAdd(BaseModel):
    ip_address: IPvAnyAddress
    type_instrument: TypeInstr


class SInstrInfo(SInstrumentsAdd):
    model: str
    ser_num: str
