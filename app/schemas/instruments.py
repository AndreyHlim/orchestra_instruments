from typing import Optional

from pydantic import BaseModel
from schemas.generators import SInstrInfo


class Instruments(BaseModel):
    signal_generator: Optional[SInstrInfo] = None
    sound_generator: Optional[SInstrInfo] = None
    spectrum_analizer: Optional[str] = None
