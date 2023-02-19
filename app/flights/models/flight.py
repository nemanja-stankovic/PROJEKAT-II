from sqlalchemy import Column, String, ForeignKey, Integer, Date, DateTime
from uuid import uuid4
from app.db import Base
from sqlalchemy.orm import relationship
from datetime import datetime

class Flight(Base):
    __tablename__ = "flights"
    flight_id = Column(String(50), primary_key=True, default=uuid4)
    departure_time = Column(DateTime)
    arrival_time = Column(DateTime)
    airline = Column(String(50))
    num_of_seats = Column(Integer)
    route_id = Column(String(50), ForeignKey( "flight_routes.route_id"))
    route = relationship("Route", lazy="subquery")


    def __init__(self, departure_time: str, arrival_time: str, airline, num_of_seats, route_id ):
        self.departure_time = datetime.strptime(departure_time, "%Y-%m-%d-%H-%M")
        self.arrival_time = datetime.strptime(arrival_time, "%Y-%m-%d-%H-%M")
        self.airline = airline
        self.num_of_seats = num_of_seats
        self.route_id =route_id



