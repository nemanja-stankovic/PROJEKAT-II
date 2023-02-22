"""This function is used to deserialize the JSON data from the API into a Python object."""
from pydantic import BaseModel, UUID4



class AirportSchema(BaseModel):
    """This class is a model for the Airport table in the database"""
    airport_id: UUID4
    airport_name: str
    city: str
    country: str
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


class AirportSchemaIn(BaseModel):
    """This class is used to deserialize the JSON data from the API into a Python object"""
    airport_name: str
    city: str
    country: str
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
