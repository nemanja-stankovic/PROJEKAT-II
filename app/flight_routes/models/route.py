from sqlalchemy import Column, String, ForeignKey, CheckConstraint
from uuid import uuid4
from app.db import Base
from sqlalchemy.orm import relationship


class Route(Base):
    __tablename__ = "flight_routes"
    route_id = Column(String(50), primary_key=True, default=uuid4)
    from_airport_id = Column(String(50), ForeignKey( "airports.airport_id"))
    to_airport_id = Column(String(50), ForeignKey("airports.airport_id"))
    # airport = relationship("Airport", lazy="subquery")

    def __init__(self, from_airport_id, to_airport_id):
        self.from_airport_id = from_airport_id
        self.to_airport_id = to_airport_id

