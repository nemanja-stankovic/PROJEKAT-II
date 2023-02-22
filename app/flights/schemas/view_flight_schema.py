from pydantic import BaseModel, UUID4
from datetime import datetime

class ViewFlightSchema(BaseModel):
    # view_flight_id: str
    flight_id: str
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

    class Config:
        orm_mode = True
