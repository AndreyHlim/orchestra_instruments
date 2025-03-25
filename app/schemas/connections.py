from enum import Enum

from pydantic import BaseModel, ConfigDict, Field, IPvAnyAddress
from pyvisa.resources import Resource


class TypeInstr(str, Enum):
    signal_generator = 'Generator Signals'
    sound_generator = 'Generator Sounds'
    spectrum_analizer = 'Spectrum Analyzer'


class SInstrumentsAdd(BaseModel):
    ip_address: IPvAnyAddress
    type_instrument: TypeInstr


class SInstrInfo(SInstrumentsAdd):
    model: str
    port: str
    is_connect: bool
    resource: Resource = Field(exclude=True)
    model_config = ConfigDict(arbitrary_types_allowed=True)

    @classmethod
    def sernum(self):
        return self.resource(
            self.type_instrument.name
        ).query('*IDN?')
