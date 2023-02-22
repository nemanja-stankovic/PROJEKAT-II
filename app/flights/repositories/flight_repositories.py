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
        flights = self.db.query(Flight).all()
        return flights

    def read_flight_by_id(self, flight_id: str):
        try:
            flight = self.db.query(Flight).filter(Flight.flight_id == flight_id).first()
            if flight is None:
                raise FlightNotFoundException(f"Flight with provided ID: {flight_id} not found.", 400)
            return flight
        except Exception as e:
            print(str(e))
            raise(e)

    def read_flights_by_route_id(self, route_id: str):   # ne radi !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        flights = self.db.query(Flight).filter(Flight.route_id == route_id).all()
        if bool(flights) is False:
            raise FlightNotFoundException(f"Flight with provided route ID: {route_id} not found.", 400)
        else:
            return flights

    def read_flights_by_departure_date(self, departure_date: str):
        flights = self.db.query(Flight).filter(Flight.departure_time.ilike(f"%{departure_date}%")).all()
        if bool(flights) is False:
            raise FlightNotFoundException(f"Flight with provided departure_date: {departure_date} not found.", 400)
        else:
            return flights

    def read_flights_by_arrival_date(self, arrival_date: str):
        flights = self.db.query(Flight).filter(Flight.arrival_time.ilike(f"%{arrival_date}%")).all()
        if bool(flights) is False:
            raise FlightNotFoundException(f"Flight with provided arrival date: {arrival_date} not found.", 400)
        else:
            return flights
    def read_available_flights_by_departure_date(self, departure_date: str):
        flights = self.db.query(Flight).filter(Flight.departure_time.ilike(f"%{departure_date}%")).join(Ticket).filter(Ticket.is_it_reserved == False).all()
        if bool(flights) is False:
            raise FlightNotFoundException(f"Flight with provided departure_date: {departure_date} not found.", 400)
        else:
            return flights

    def read_flight_cities_and_date(self, from_city: str, to_city: str, departure_date: str):
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
        try:
            flight = self.db.query(Flight).filter(Flight.flight_id == flight_id).first()
            if flight is None:
                raise FlightNotFoundException(f"Flight with provided ID: {flight_id} not found.", 400)
            self.db.delete(flight)
            self.db.commit()
            return True
        except Exception as e:
            raise e
