from app.flights.models import Flight
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.flights.exceptions import FlightNotFoundException
from app.tickets.models import Ticket
from app.flight_routes.models import Route
from app.airports.models import Airport

class FlightRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_flight(self, departure_time, arrival_time, airline, num_of_seats, route_id):
        """
        It creates a flight object and adds it to the database
        @param departure_time - The time the flight is scheduled to depart.
        @param arrival_time - The time the flight arrives at the destination.
        @param airline - The name of the airline
        @param num_of_seats - The number of seats available on the flight.
        @param route_id - The id of the route that the flight is on.
        @returns The flight object is being returned.
        """
        try:
            flight = Flight(departure_time=departure_time, arrival_time=arrival_time, airline=airline,
                            num_of_seats=num_of_seats, route_id=route_id)
            self.db.add(flight)
            self.db.commit()
            self.db.refresh(flight)
            return flight
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    def read_all_flights(self):
        """
        It returns all the flights in the database
        @returns A list of all the flights in the database.
        """
        flights = self.db.query(Flight).all()
        return flights

    def read_flight_by_id(self, flight_id: str):
        """
        It takes a flight_id as a string, and returns a flight object
        @param {str} flight_id - The ID of the flight to be read.
        @returns A flight object
        """
        try:
            flight = self.db.query(Flight).filter(Flight.flight_id == flight_id).first()
            if flight is None:
                raise FlightNotFoundException(f"Flight with provided ID: {flight_id} not found.", 400)
            return flight
        except Exception as e:
            print(str(e))
            raise(e)

    def read_flights_by_route_id(self, route_id: str):   # ne radi !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        """
        It returns all flights that have a route_id that matches the route_id provided as an argument
        @param {str} route_id - str
        @returns A list of flights.
        """
        flights = self.db.query(Flight).filter(Flight.route_id == route_id).all()
        if bool(flights) is False:
            raise FlightNotFoundException(f"Flight with provided route ID: {route_id} not found.", 400)
        else:
            return flights

    def read_flights_by_departure_date(self, departure_date: str):
        """
        It returns a list of flights that match the provided departure date
        @param {str} departure_date - str
        @returns A list of flights with the same departure date.
        """
        flights = self.db.query(Flight).filter(Flight.departure_time.ilike(f"%{departure_date}%")).all()
        if bool(flights) is False:
            raise FlightNotFoundException(f"Flight with provided departure_date: {departure_date} not found.", 400)
        else:
            return flights

    def read_flights_by_arrival_date(self, arrival_date: str):
        """
        It returns a list of flights that match the provided arrival date
        @param {str} arrival_date - str
        @returns A list of flights with the arrival date matching the provided arrival date.
        """
        flights = self.db.query(Flight).filter(Flight.arrival_time.ilike(f"%{arrival_date}%")).all()
        if bool(flights) is False:
            raise FlightNotFoundException(f"Flight with provided arrival date: {arrival_date} not found.", 400)
        else:
            return flights
    def read_available_flights_by_departure_date(self, departure_date: str):
        """
        It returns all the flights that have a departure date that matches the provided departure date, and that have at
        least one unreserved ticket
        @param {str} departure_date - str
        @returns A list of flights.
        """
        flights = self.db.query(Flight).filter(Flight.departure_time.ilike(f"%{departure_date}%")).join(Ticket).filter(Ticket.is_it_reserved == False).all()
        if bool(flights) is False:
            raise FlightNotFoundException(f"Flight with provided departure_date: {departure_date} not found.", 400)
        else:
            return flights

    def read_flight_cities_and_date(self, from_city: str, to_city: str, departure_date: str):
        """
        It returns all flights that have a route that has a from_airport_id that matches the airport_id of an airport that
        has the city name of the from_city parameter, and a to_airport_id that matches the airport_id of an airport that has
        the city name of the to_city parameter, and a departure_time that matches the departure_date parameter
        @param {str} from_city - str
        @param {str} to_city - str, from_city: str, departure_date: str
        @param {str} departure_date - str
        @returns A list of flights that match the given criteria.
        """
        flights_with_routes = self.db.query(Flight).join(Route)
        flights_with_routes_with_airports = flights_with_routes.join(Airport,Airport.airport_id == Route.from_airport_id)
        flights_from = self.db.query(Flight).outerjoin(Route).outerjoin(Airport,Airport.airport_id == Route.from_airport_id).filter(Route.from_airport_id == Airport.airport_id & Airport.city == from_city).all()
        flights_to = self.db.query(Flight).outerjoin(Route).outerjoin(Airport,Airport.airport_id == Route.to_airport_id).filter(Route.to_airport_id == Airport.airport_id & Airport.city == to_city).all()
        flight_date = self.db.query(Flight).filter(Flight.departure_time.ilike(f"%{departure_date}%")).all()
        flights = self.db.query(Flight).intersect(flights_from).intersect(flights_to).intersect(flight_date)
        return flights


    # def read_available_flights_by_departure_date(self, departure_date: str):
    #     flights = self.db.query(Flight).join(Ticket).all()
    #     if bool(flights) is False:
    #         raise FlightNotFoundException(f"Flight with provided departure_date: {departure_date} not found.", 400)
    #     else:
    #         return flights

    def delete_flight(self, flight_id: str):
        """
        It deletes a flight from the database
        @param {str} flight_id - The ID of the flight to be deleted.
        @returns True
        """
        try:
            flight = self.db.query(Flight).filter(Flight.flight_id == flight_id).first()
            if flight is None:
                raise FlightNotFoundException(f"Flight with provided ID: {flight_id} not found.", 400)
            self.db.delete(flight)
            self.db.commit()
            return True
        except Exception as e:
            raise e
