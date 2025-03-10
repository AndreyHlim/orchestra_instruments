from pydantic import BaseModel, Field
from enum import Enum
from sqlalchemy.orm import Mapped
from sqlalchemy_utils import ChoiceType
from sqlalchemy import Column


class GenMode(str, Enum):
    cw = 'cw'
    fixed = 'fixed'
    sweep = 'sweep'
    list = 'list'


class Generator(BaseModel):
    MODE_GEN = [(mode.name, mode.value) for mode in GenMode]
    mode: Mapped[str] = Column(ChoiceType(MODE_GEN), default='cw', nullable=False)
    ip_address: str = Field(pattern=r'^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}$')
    ser_num: str = Field(description='Заводской номер генератора ВЧ сигналов')
    model: str = Field(
        description='Фирма-производитель и модель генератора ВЧ сигналов'
    )
    freq_ext: int = Field(
        ge=10000000,
        le=250000000,
        description='Частота выхода внешнего опорного генератора в Герцах'
    )
    ext_out: bool = Field(
        description='Состояние выхода внешнего опорного генератора'
    )
    mode: str = Field(description='Режим работы генератора ВЧ сигналов')
    freq_center: int = Field (
        ge=9000,
        le=6000000000,
        description='Размерность - Гц'
        )
    out_rf: bool = Field(
        description='Состояние выхода RF генератора ВЧ синалов'
    )
