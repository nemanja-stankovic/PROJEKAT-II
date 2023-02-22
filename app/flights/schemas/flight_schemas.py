"""`The `FlightSchema` class is a subclass of the `BaseModel` class"""
from pydantic import BaseModel, UUID4
from datetime import datetime


class FlightSchema(BaseModel):
    """The `FlightSchema` class is a subclass of the `BaseModel` class"""
    flight_id: UUID4
    departure_time: datetime
    arrival_time: datetime
    airline: str
    num_of_seats: int
    route_id: str

    def public_method_one(self):
        """
        A function definition.
        """

    def public_method_two(self):
        """
        A function definition.
        """
    class Config:
        """Config class"""
        orm_mode = True

        def public_method_one(self):
            """
            A function definition.
            """

        def public_method_two(self):
            """
            A function definition.
            """


class FlightSchemaIn(BaseModel):
    """This class is used to validate the input data for the `/flights` endpoint"""
    departure_time: str
    arrival_time: str
    airline: str
    num_of_seats: int
    route_id: str

    def public_method_one(self):
        """
        A function definition.
        """

    def public_method_two(self):
        """
        A function definition.
        """
    class Config:
        """Config class"""
        orm_mode = True
        def public_method_one(self):
            """
            A function definition.
            """

        def public_method_two(self):
            """
            A function definition.
            """


