from app.flights.models import UserViewFlight
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

class UserViewFlightRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_user_view_flight(self, departure_time: str,arrival_time: str, airline, num_of_seats,
                           num_of_available_tickets_first_class: int, num_of_available_tickets_second_class: int,
                           price_first_class: float , price_second_class: float, from_city: str, to_city: str, user_id):
        """
        It creates a new view flight object and adds it to the database.  """
        try:
            user_view_flight = UserViewFlight( departure_time=departure_time,arrival_time=arrival_time,
                                     airline=airline, num_of_seats=num_of_seats,
                                     num_of_available_tickets_first_class=num_of_available_tickets_first_class,
                                     num_of_available_tickets_second_class=num_of_available_tickets_second_class,
                                     price_first_class=price_first_class, price_second_class=price_second_class,
                                     from_city=from_city, to_city=to_city, user_id=user_id)
            self.db.add(user_view_flight)
            self.db.commit()
            self.db.refresh(user_view_flight)
            return user_view_flight
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    def read_all_user_view_flights(self):
        """
        It returns all the flights in the database
        @returns A list of all the flights in the database.
        """
        try:
            user_view_flights = self.db.query(UserViewFlight).all()
            return user_view_flights
        except Exception as e:
            raise e
    def sort_user_view_flight_by_price(self):
        """
        It sorts the view_flights by price_second_class.
        @returns A list of all the flights in the database, sorted by price.
        """
        try:
            user_view_flights = self.db.query(UserViewFlight).order_by(UserViewFlight.price_second_class).all()
            return user_view_flights
        except Exception as e:
            raise e

    def delete_all_user_view_flights(self):
        """
        It deletes all the rows in the UserViewFlight table
        :return: A list of all the user_view_flights in the database.
        """
        try:
            user_view_flights = self.db.query(UserViewFlight).all()
            self.db.delete(user_view_flights)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def delete_all_user_view_flights_by_user_id(self, user_id: str):
        """
        It deletes all the rows in the UserViewFlight table
        :return: A list of all the user_view_flights in the database.
        """
        try:
            user_view_flights = self.db.query(UserViewFlight).filter(UserViewFlight.user_id == user_id).all()
            for user_view_flight in user_view_flights:
                self.db.delete(user_view_flight)
                self.db.commit()
            return True
        except Exception as e:
            raise e


