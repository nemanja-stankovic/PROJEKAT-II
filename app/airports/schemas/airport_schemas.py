from pydantic import BaseModel, UUID4


class AirportSchema(BaseModel):
    airport_id: UUID4
    airport_name: str
    city: str
    country: str

    class Config:
        orm_mode = True


# > This class is used to deserialize the JSON data from the API into a Python object
class AirportSchemaIn(BaseModel):
    airport_name: str
    city: str
    country: str

    class Config:
        orm_mode = True
