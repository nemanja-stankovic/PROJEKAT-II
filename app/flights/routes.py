from fastapi import APIRouter
from app.flights.controller import FlightController
from app.flights.schemas import FlightSchema, FlightSchemaIn, SearchedFlightSchema


flight_router = APIRouter(tags=["Flights"], prefix="/api/flights")


@flight_router.post("/create-new-flight", response_model=FlightSchema)
def create_new_flight(flight: FlightSchemaIn):
    return FlightController.create_new_flight(departure_time=flight.departure_time, arrival_time=flight.arrival_time,
                                              num_of_seats=flight.num_of_seats, route_id=flight.route_id,
                                              airline=flight.airline)


@flight_router.get("/searche-flight-something", response_model=list[SearchedFlightSchema])
def search_flights_by_cities(from_city, to_city):
    flights = FlightController.search_flights_by_cities(from_city, to_city)
    return flights


@flight_router.get("/get-flight-by-id", response_model=FlightSchema)
def get_flight_by_id(flight_id: str):
    return FlightController.get_flight_by_id(flight_id)

@flight_router.get("/search-flights-by-starting-point", response_model=list[FlightSchema])
def search_flights_by_from_city(from_city):
    return FlightController.search_flights_by_from_city(from_city)

@flight_router.get("/search-flights-by-destination", response_model=list[FlightSchema])
def search_flights_by_to_city(to_city):
    return FlightController.search_flights_by_to_city(to_city)

@flight_router.get("/search-flights-by-destination", response_model=list[FlightSchema])
def search_flights_by_to_city(to_city):
    return FlightController.search_flights_by_to_city(to_city)

@flight_router.get("/search-flights-by-departure-date", response_model=list[FlightSchema])
def search_flights_by_departure_date(departure_date):
    return FlightController.search_flights_by_departure_date(departure_date)

@flight_router.delete("/delete-flight")
def delete_flight_by_id(flight_id: str):
    return FlightController.delete_flight_by_id(flight_id)
