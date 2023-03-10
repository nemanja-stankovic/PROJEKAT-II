from fastapi import APIRouter, Depends
from app.airports.controller import AirportController
from app.airports.schemas import AirportSchema, AirportSchemaIn
from app.users.controller.user_auth_controller import JWTSuperUserBearer

airport_router = APIRouter(tags=["Airports"], prefix="/api/airports")


@airport_router.post("/create-new-airport", response_model=AirportSchema, dependencies=[Depends(JWTSuperUserBearer())])
def create_new_airport(airport: AirportSchemaIn):
    return AirportController.create_new_airport(airport_name=airport.airport_name, city=airport.city, country=airport.country)

@airport_router.get("/get-all-airports", response_model=list[AirportSchema], dependencies=[Depends(JWTSuperUserBearer())])
def get_all_airports():
    airports = AirportController.get_all_airports()
    return airports

@airport_router.get("/get-all-airports-with-city", response_model=list[AirportSchema], dependencies=[Depends(JWTSuperUserBearer())])
def get_all_airports_with_city(city):
    airports = AirportController.get_all_airports_with_city(city=city)
    return airports

@airport_router.get("/get-airport-by-id", response_model=AirportSchema, dependencies=[Depends(JWTSuperUserBearer())])
def get_airport_by_id(airport_id: str):
    return AirportController.get_airport_by_id(airport_id)

@airport_router.get("/get-airport-by-name", response_model=AirportSchema, dependencies=[Depends(JWTSuperUserBearer())])
def get_airport_by_name(airport_name: str):
    return AirportController.get_airport_by_name(airport_name)

@airport_router.delete("/delete-airport", dependencies=[Depends(JWTSuperUserBearer())])
def delete_airport_by_id(airport_id: str):
    return AirportController.delete_airport_by_id(airport_id)

