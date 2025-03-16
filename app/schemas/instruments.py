from typing import Optional

from pydantic import BaseModel, Field

from schemas.generators import SGeneratorInfo
from schemas.sounds import SSoundGenInfo


class Instruments(BaseModel):
    signal_generator: Optional[SGeneratorInfo] = Field(default=None)
    sound_generator: Optional[SSoundGenInfo] = Field(default=None)
    spectrum_analizer: Optional[str] = Field(default=None)
