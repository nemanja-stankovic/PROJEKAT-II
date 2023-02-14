from fastapi import APIRouter
from app.airports.controller import AirportController
from app.airports.schemas import AirportSchema, AirportSchemaIn


airport_router = APIRouter(tags=["Airports"], prefix="/api/airports")


@airport_router.post("/create-new-airport", response_model=AirportSchema)
def create_new_airport(airport: AirportSchemaIn):
    return AirportController.create_new_airport(airport_name=airport.airport_name, city=airport.city, country=airport.country)


@airport_router.get("/get-all-airports", response_model=list[AirportSchema])
def get_all_airports():
    airports = AirportController.get_all_airports()
    return airports


@airport_router.get("/get-airport-by-id", response_model=AirportSchema)
def get_airport_by_id(airport_id: str):
    return AirportController.get_airport_by_id(airport_id)


@airport_router.delete("/delete-airport")
def delete_airport_by_id(airport_id: str):
    return AirportController.delete_airport_by_id(airport_id)

