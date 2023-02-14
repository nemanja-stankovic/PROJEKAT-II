# from pydantic import BaseModel, UUID4
#
#
# class RouteSchema(BaseModel):
#     airport_ID: UUID4
#     from_airport_id: str
#     to_airport_id: str
#     country: str
#
#     class Config:
#         orm_mode = True
#
#
# # > This class is used to deserialize the JSON data from the API into a Python object
# class RouteSchemaIn(BaseModel):
#     from_airport_id: str
#     to_airport_id: str
#
#     class Config:
#         orm_mode = True
