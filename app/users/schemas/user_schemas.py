"""`UserSchema` is a `BaseModel` that has an `id` of type `UUID4`, an `email` of type `str`,
    a `password` of type `str`, an`is_active` of type `bool`, and an `is_superuser` of type `bool`"""
from pydantic import BaseModel
from pydantic import UUID4, EmailStr




class UserSchema(BaseModel):
    """`UserSchema` is a `BaseModel` that has an `id` of type `UUID4`, an `email` of type `str`,
     a `password` of type `str`, an`is_active` of type `bool`, and an `is_superuser` of type `bool`"""
    id: UUID4
    email: str
    password: str
    is_active: bool
    is_superuser: bool

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

class UserSchemaIn(BaseModel):
    """A class that inherits from the BaseModel class."""
    email: EmailStr
    password: str
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
