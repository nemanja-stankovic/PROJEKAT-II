from sqlalchemy import Column, String, ForeignKey, Integer, Float, CheckConstraint, Boolean
from uuid import uuid4
from app.db import Base
from sqlalchemy.orm import relationship


class Ticket(Base):
    __tablename__ = "tickets"
    ticket_id = Column(String(50), primary_key=True, default=uuid4)
    class_number = Column(Integer)
    ticket_price = Column(Float)
    is_it_reserved = Column(Boolean)
    flight_id = Column(String(50), ForeignKey( "flights.flight_id"))
    flight = relationship("Flight", lazy="subquery")
    __table_args__ = (CheckConstraint(class_number.in_([1, 2])),)

    def __init__(self, class_number: int, ticket_price: float, flight_id: str, is_it_reserved: bool = False):
        self.class_number = class_number
        self.ticket_price = ticket_price
        self.flight_id = flight_id
        self.is_it_reserved = is_it_reserved
