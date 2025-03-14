from pydantic import BaseModel, Field


class SInstumentsAdd(BaseModel):
    ip_address: str = Field(description='IP-адрес подключаемого прибора')