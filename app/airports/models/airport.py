from sqlalchemy import Column, String
from uuid import uuid4
from app.db import Base
from sqlalchemy.orm import relationship

class Airport(Base):
    __tablename__ = "airports"
    airport_id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    airport_name = Column(String(100), unique=True)
    city = Column(String(100))
    country = Column(String(100))

    def __init__(self, airport_name, city, country):
        self.airport_name = airport_name
        self.city = city
        self.country = country
