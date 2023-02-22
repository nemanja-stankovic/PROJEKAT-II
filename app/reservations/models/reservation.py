from sqlalchemy import Column, String, ForeignKey, Integer, Date, DateTime
from uuid import uuid4
from app.db import Base
from sqlalchemy.orm import relationship


class Reservation(Base):
    __tablename__ = "reservations"
    reservation_id = Column(String(50), primary_key=True, default=uuid4)
    ticket_id = Column(String(50), ForeignKey( "tickets.ticket_id"))
    user_id = Column(String(50), ForeignKey("users.id"))
    ticket = relationship("Ticket", lazy="subquery")
    users = relationship("User", lazy="subquery")

    def __init__(self, ticket_id: str, user_id: str ):
        self.ticket_id = ticket_id
        self.user_id = user_id


