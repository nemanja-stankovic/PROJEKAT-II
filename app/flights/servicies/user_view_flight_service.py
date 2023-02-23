from app.db import SessionLocal
from app.flights.repositories import UserViewFlightRepository


class UserViewFlightService:

    @staticmethod
    def create_new_user_view_flight( departure_time: str,arrival_time: str, airline, num_of_seats,
                           num_of_available_tickets_first_class: int, num_of_available_tickets_second_class: int,
                           price_first_class: float, price_second_class: float, from_city: str, to_city: str, user_id: str):
        """ It creates a new view flight in the database  """
        try:
            with SessionLocal() as db:
                repository = UserViewFlightRepository(db)

                return repository.create_user_view_flight(departure_time,arrival_time, airline, num_of_seats,
                           num_of_available_tickets_first_class, num_of_available_tickets_second_class,
                           price_first_class, price_second_class, from_city, to_city, user_id)
        except Exception as e:
            raise e

    @staticmethod
    def sort_user_view_flights_by_price():
        """
        It sorts the flights by price.
        """
        try:
            with SessionLocal() as db:
                repository = UserViewFlightRepository(db)
                return repository.sort_user_view_flight_by_price()
        except Exception as e:
            raise e

