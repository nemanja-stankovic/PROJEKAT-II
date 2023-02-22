from pydantic import BaseModel, UUID4
from app.users.schemas import UserSchema
from app. tickets.schemas import TicketSchema
from app.users.models import User
from app.tickets.models import Ticket

class ReservationSchema(BaseModel):
    resevation_id: UUID4
    ticket_id: str
    user_id: str
    # users: User
    # tickets: Ticket
    class Config:
        orm_mode = True


class ReservationSchemaIn(BaseModel):
    ticket_id: str
    user_id: str

    class Config:
        orm_mode = True

