from enum import Enum

from pydantic import BaseModel, IPvAnyAddress


class TypeInstr(str, Enum):
    generator_signals = 'Generator Signals'
    generator_sounds = 'Generator Sounds'
    spectrum_analyzer = 'Spectrum Analyzer'


class SInstrumentsAdd(BaseModel):
    ip_address: IPvAnyAddress
    type_instrument: TypeInstr


class SInstrInfo(SInstrumentsAdd):
    model: str
    ser_num: str
