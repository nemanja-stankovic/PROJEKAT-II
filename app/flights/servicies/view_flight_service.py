from app.db import SessionLocal
from app.flights.repositories import ViewFlightRepository


class ViewFlightService:

    @staticmethod
    def create_new_view_flight(flight_id: str, departure_time: str,arrival_time: str, airline, num_of_seats,
                           num_of_available_tickets_first_class: int, num_of_available_tickets_second_class: int,
                           price_first_class: float, price_second_class: float, from_city: str, to_city: str):
        try:
            with SessionLocal() as db:
                repository = ViewFlightRepository(db)

                return repository.create_view_flight(flight_id, departure_time,arrival_time, airline, num_of_seats,
                           num_of_available_tickets_first_class, num_of_available_tickets_second_class,
                           price_first_class, price_second_class, from_city, to_city)
        except Exception as e:
            raise e

    @staticmethod
    def sort_view_flights_by_price():
        try:
            with SessionLocal() as db:
                repository = ViewFlightRepository(db)
                return repository.sort_view_flight_by_price()
        except Exception as e:
            raise e

    @staticmethod
    def delete_view_flight():
        try:
            with SessionLocal() as db:
                repository = ViewFlightRepository(db)
                return repository.delete_view_flight()
        except Exception as e:
            raise e