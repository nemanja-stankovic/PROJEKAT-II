""" `ReservationSchema` is a class that inherits from `BaseModel`"""
from pydantic import BaseModel, UUID4


class ReservationSchema(BaseModel):
    """ReservationSchema` is a class that inherits from `BaseModel"""
    reservation_id: UUID4
    ticket_id: str
    user_id: str
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



class ReservationSchemaIn(BaseModel):
    """ReservationSchemaIn` is a class that inherits from `BaseModel"""
    ticket_id: str
    user_id: str

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
