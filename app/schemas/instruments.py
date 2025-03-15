from typing import Optional

from pydantic import BaseModel

from schemas.generators import SGeneratorAdd


class Instruments(BaseModel):
    signal_generator: Optional[SGeneratorAdd]
    sound_generator: Optional[str]
    spectrum_analizer: Optional[str]
