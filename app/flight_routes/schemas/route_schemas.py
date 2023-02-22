"""A RouteSchema class that inherits from BaseModel"""
from pydantic import BaseModel, UUID4



class RouteSchema(BaseModel):
    """This class is a model for a route"""
    route_id: UUID4
    from_airport_id: str
    to_airport_id: str

    def public_method_one(self):
        """
        A function definition.
        """

    def public_method_two(self):
        """
        A function definition.
        """
    class Config:
        """Config Class"""
        orm_mode = True

        def public_method_one(self):
            """
            A function definition.
            """

        def public_method_two(self):
            """
            A function definition.
            """

class RouteSchemaIn(BaseModel):
    from_airport_id: str
    to_airport_id: str

    def public_method_one(self):
        """
        A function definition.
        """

    def public_method_two(self):
        """
        A function definition.
        """
    class Config:
        """Config Class"""
        orm_mode = True

        def public_method_one(self):
            """
            A function definition.
            """

        def public_method_two(self):
            """
            A function definition.
            """
