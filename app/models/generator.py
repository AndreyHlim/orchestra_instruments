from pydantic import BaseModel, Field
from enum import Enum


class GenMode(str, Enum):
    cw = 'cw'
    fixed = 'fixed'
    sweep = 'sweep'
    list = 'list'


class GeneratorsRF(BaseModel):
    ip_address: str
    ser_num: str = Field(
        description='Заводской номер генератора ВЧ сигналов'
    )
    model: str = Field(
        description='Фирма-производитель и модель генератора ВЧ сигналов'
    )
    mode_work: GenMode = Field(
        default=GenMode.cw,
        description='Выбор режимаработы генератора ВЧ сигналов'
    )
    freq_ext: int = Field(
        ge=10000000,
        le=250000000,
        default=10000000,
        description='Частота выхода внешнего опорного генератора в Герцах'
    )
    ext_out: bool = Field(
        default=False,
        description='Состояние выхода внешнего опорного генератора'
    )
    freq_center: int = Field (
        ge=9000,
        le=6000000000,
        default=100000000,
        description='Размерность - Гц'
    )
    out_rf_lvl: int = Field(
        ge=-40,
        le=25,
        default=-20,
        description='Выходная мощность генератора ВЧ сигналов на выходе RF'
    )
    out_rf_status: bool = Field(
        default=False,
        description='Состояние выхода RF генератора ВЧ синалов'
    )
