from sqlalchemy import Column, String, Integer, DateTime, Float
from app.db import Base
from uuid import uuid4


class ViewFlight(Base):
    __tablename__ = "view_flights"
    # view_flight_id = Column(String(50), primary_key=True, default=uuid4)
    flight_id = Column(String(50), primary_key=True)
    departure_time = Column(String(50) )
    arrival_time = Column(String(50))
    airline = Column(String(50))
    num_of_seats = Column(Integer)
    num_of_available_tickets_first_class = Column(Integer)
    num_of_available_tickets_second_class = Column(Integer)
    price_first_class = Column(Float)
    price_second_class = Column(Float)
    from_city = Column(String(50))
    to_city = Column(String(50))

    def __init__(self, flight_id: str, departure_time: str,arrival_time: str, airline, num_of_seats,
                 num_of_available_tickets_first_class: int, num_of_available_tickets_second_class: int,
                 price_first_class: float, price_second_class: float, from_city: str, to_city: str ):
        self.flight_id = flight_id
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
