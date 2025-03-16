from typing import Optional

from pydantic import BaseModel

from schemas.generators import SGeneratorInfo
from schemas.sounds import SSoundGenInfo


class Instruments(BaseModel):
    signal_generator: Optional[SGeneratorInfo] = None
    sound_generator: Optional[SSoundGenInfo] = None
    spectrum_analizer: Optional[str] = None
