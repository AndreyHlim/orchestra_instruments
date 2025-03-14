from pydantic import BaseModel, Field


class GeneratorsRF(BaseModel):
    ip_address: str
    ser_num: str = Field(
        description='Заводской номер генератора ВЧ сигналов'
    )
    model: str = Field(
        description='Фирма-производитель и модель генератора ВЧ сигналов'
    )
