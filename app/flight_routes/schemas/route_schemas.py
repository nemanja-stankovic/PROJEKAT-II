from pydantic import BaseModel, UUID4


class RouteSchema(BaseModel):
    route_id: UUID4
    from_airport_id: str
    to_airport_id: str

    class Config:
        orm_mode = True


class RouteSchemaIn(BaseModel):
    from_airport_id: str
    to_airport_id: str

    class Config:
        orm_mode = True
