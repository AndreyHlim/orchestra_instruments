from enum import Enum

from pydantic import BaseModel


class TypeInstr(str, Enum):
    generator_signals = 'Generator Signals'
    generator_sounds = 'Generator Sounds'
    spectrum_analyzer = 'Spectrum Analyzer'


class SInstumentsAdd(BaseModel):
    ip_address: str
    type_instrument: TypeInstr
