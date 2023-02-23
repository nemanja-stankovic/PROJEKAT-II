from sqlalchemy import Column, String, Integer,ForeignKey, Float
from app.db import Base
from sqlalchemy.orm import relationship
from uuid import uuid4

class UserViewFlight(Base):
    __tablename__ = "user_view_flights"
    view_flight_id = Column(String(50), primary_key=True, default=uuid4)
    departure_time = Column(String(50))
    arrival_time = Column(String(50))
    airline = Column(String(50))
    num_of_seats = Column(Integer)
    num_of_available_tickets_first_class = Column(Integer)
    num_of_available_tickets_second_class = Column(Integer)
    price_first_class = Column(Float)
    price_second_class = Column(Float)
    from_city = Column(String(50))
    to_city = Column(String(50))
    user_id = Column(String(50), ForeignKey( "users.id"))
    user = relationship("User", lazy="subquery")

    def __init__(self, departure_time: str,arrival_time: str, airline, num_of_seats,
                 num_of_available_tickets_first_class: int, num_of_available_tickets_second_class: int,
                 price_first_class: float, price_second_class: float, from_city: str, to_city: str, user_id: str ):
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.airline = airline
        self.num_of_seats = num_of_seats
        self.num_of_available_tickets_first_class = num_of_available_tickets_first_class
        self.num_of_available_tickets_second_class = num_of_available_tickets_second_class
        self.price_first_class = price_first_class
        self.price_second_class = price_second_class
        self.from_city = from_city
        self.to_city = to_city
        self.user_id = user_id

