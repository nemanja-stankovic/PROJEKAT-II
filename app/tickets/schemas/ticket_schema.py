from pydantic import BaseModel, UUID4



class TicketSchema(BaseModel):
    ticket_id: UUID4
    class_number: int
    ticket_price: float
    flight_id: str
    is_it_reserved: bool

    class Config:
        orm_mode = True


class TicketSchemaIn(BaseModel):
    class_number: int = 2
    ticket_price: float
    flight_id: str
    is_it_reserved: bool = False

    class Config:
        orm_mode = True

