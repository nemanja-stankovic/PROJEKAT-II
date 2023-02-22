from pydantic import BaseModel, UUID4
from datetime import datetime

class FlightSchema(BaseModel):
    flight_id: UUID4
    departure_time: datetime
    arrival_time: datetime
    airline: str
    num_of_seats: int
    route_id: str
    class Config:
        orm_mode = True


class FlightSchemaIn(BaseModel):
    departure_time: str
    arrival_time: str
    airline: str
    num_of_seats: int
    route_id: str

    class Config:
        orm_mode = True


