from app.flights.models import Flight
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.flights.exceptions import FlightNotFoundException


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
        flight = self.db.query(Flight).filter(Flight.flight_id == flight_id).first()
        if flight is None:
            raise FlightNotFoundException(f"Flight with provided ID: {flight_id} not found.", 400)
        return flight

    def read_flights_by_route_id(self, route_id: str):
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
