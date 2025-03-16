from enum import Enum

from pydantic import Field

from schemas.connections import SInstrInfo, TypeInstr


class TypeLFSignals(str, Enum):
    sinus = 'SINusoid'
    square = 'SQUare'
    ramp = 'RAMP'
    pulse = 'PULSe'
    noise = 'NOISe'
    dc = 'DC'


class UnitOut(str, Enum):
    vpp = 'VPP'
    vrms = 'VRMS'
    dbm = 'DBM'


class SSoundGenInfo(SInstrInfo):
    type_instrument: TypeInstr = Field(default=TypeInstr.generator_sounds)


class SSoundGenAdd(SSoundGenInfo):
    out_status: bool = Field(default=False)
    out_lvl: int = Field(ge=0, le=3, default=3)
    unit_out: UnitOut = Field(default=UnitOut.vpp)
    freq: float = Field(ge=0.000001, le=20000000, default=1025)
    type_signal: TypeLFSignals = Field(default=TypeLFSignals.sinus)
