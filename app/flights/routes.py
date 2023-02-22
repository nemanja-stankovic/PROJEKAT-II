from fastapi import APIRouter
from app.flights.controller import FlightController
from app.tickets.controller import TicketController
from app.flights.schemas import FlightSchema, FlightSchemaIn, ViewFlightSchema
from app.tickets.schemas import TicketSchema

flight_router = APIRouter(tags=["Flights"], prefix="/api/flights")


@flight_router.post("/create-new-flight", response_model=FlightSchema)
def create_new_flight(flight: FlightSchemaIn):
    return FlightController.create_new_flight(departure_time=flight.departure_time, arrival_time=flight.arrival_time,
                                              num_of_seats=flight.num_of_seats, route_id=flight.route_id,
                                              airline=flight.airline)

# @flight_router.get("/searche-flight-by-cities", response_model=list[SearchedFlightSchema]) #ne radi
# def search_flights_by_cities(from_city, to_city):
#     flights = FlightController.search_flights_by_cities(from_city, to_city)
#     return flights


@flight_router.get("/get-flight-by-id", response_model=FlightSchema)
def get_flight_by_id(flight_id: str):
    return FlightController.get_flight_by_id(flight_id)

@flight_router.get("/get-flight-by-route-id", response_model=list[FlightSchema])
def get_flight_by_route_id(route_id: str):
    return FlightController.search_flights_by_route_id(route_id)

@flight_router.get("/get-number-of-available-tickets-by-flight-id", response_model=int)
def get_number_of_available_tickets(flight_id: str):
    return TicketController.get_number_of_available_tickets_by_flight_id(flight_id)
@flight_router.get("/get-all-flights", response_model=list[FlightSchema])
def get_all_flights():
    return FlightController.get_all_flights()

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

@flight_router.get("/search-available-flights-by-departure-date", response_model=list[FlightSchema])
def search_available_flights_by_departure_date(departure_date):
    return FlightController.search_available_flights_by_departure_date(departure_date)

@flight_router.get("/search-flights-by-cities-and-dates",response_model=list[ViewFlightSchema])
def search_flights_by_cities_and_dates(from_city, to_city,departure_date, arrival_date):
    return FlightController.search_flights_by_cities_and_dates(from_city, to_city, departure_date, arrival_date)

@flight_router.get("/explore-everywhere", response_model=list[ViewFlightSchema])
def explore_everywhere(departure_date, from_city):
    return FlightController.explore_everywhere(departure_date, from_city)

@flight_router.put("/update-ticket-price", response_model=list[TicketSchema])
def update_ticket_price(flight_id, class_number, price):
    return TicketController.update_ticket_price(flight_id=flight_id, class_number=class_number, price=price)

@flight_router.delete("/delete-flight")
def delete_flight_by_id(flight_id: str):
    return FlightController.delete_flight_by_id(flight_id)


