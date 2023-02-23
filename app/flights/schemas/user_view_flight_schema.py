from pydantic import BaseModel, UUID4


class UserViewFlightSchema(BaseModel):
    view_flight_id: UUID4
    departure_time: str
    arrival_time: str
    airline: str
    num_of_seats: int
    num_of_available_tickets_first_class: int
    num_of_available_tickets_second_class: int
    price_first_class: float
    price_second_class: float
    from_city: str
    to_city: str
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
        orm_mode = True

        def public_method_one(self):
            """
            A function definition.
            """

        def public_method_two(self):
            """
            A function definition.
            """