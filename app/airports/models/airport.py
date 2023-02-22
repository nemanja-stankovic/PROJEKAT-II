from uuid import uuid4
from sqlalchemy import Column, String
from app.db import Base



class Airport(Base):
    """Airport is a class that inherits from Base"""
    __tablename__ = "airports"
    airport_id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    airport_name = Column(String(100), unique=True)
    city = Column(String(100))
    country = Column(String(100))

    def __init__(self, airport_name, city, country):
        """
        The function __init__() is a special function in Python classes. It is known as a constructor in object oriented
        concepts. This function is called when an object is created from a class and it allows the class to initialize the
        attributes of the class.
        @param airport_name - The name of the airport.
        @param city - The city the airport is located in.
        @param country - The country the airport is located in.
        """
        self.airport_name = airport_name
        self.city = city
        self.country = country

    def public_method_one(self):
        """
        A function definition.
        """
