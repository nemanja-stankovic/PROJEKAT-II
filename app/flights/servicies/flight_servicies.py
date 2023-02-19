from sqlalchemy.exc import IntegrityError

from app.flights.models import Flight
from app.db import SessionLocal
from app.flights.repositories import FlightRepository
from app.flights.exceptions import FlightExceptionCode


class FlightService:

    @staticmethod
    def create_new_flight(departure_time, arrival_time, airline, num_of_seats, route_id):
        try:
            with SessionLocal() as db:
                repository = FlightRepository(db)
                return repository.create_flight(departure_time, arrival_time, airline, num_of_seats, route_id)
        except Exception as e:
            raise e


    @staticmethod
    def read_all_flights():
        try:
            with SessionLocal() as db:
                repository = FlightRepository(db)
                return repository.read_all_flights()
        except Exception as e:
            raise e

    @staticmethod
    def read_flight_by_id(flight_id):
        try:
            with SessionLocal() as db:
                repository = FlightRepository(db)
                return repository.read_flight_by_id(flight_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_flights_by_route_id(route_id):
        try:
            with SessionLocal() as db:
                repository = FlightRepository(db)
                return repository.read_flights_by_route_id(route_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_flights_by_departure_date(departure_date):
        try:
            with SessionLocal() as db:
                repository = FlightRepository(db)
                return repository.read_flights_by_departure_date(departure_date)
        except Exception as e:
            raise e

    @staticmethod
    def delete_flight_by_id(flight_id):
        try:
            with SessionLocal() as db:
                repository = FlightRepository(db)
                return repository.delete_flight(flight_id)
        except Exception as e:
            raise e
