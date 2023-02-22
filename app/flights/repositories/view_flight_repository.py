from app.flights.models import ViewFlight
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.flights.exceptions import FlightNotFoundException
from app.tickets.models import Ticket

class ViewFlightRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_view_flight(self, flight_id: str, departure_time: str,arrival_time: str, airline, num_of_seats,
                           num_of_available_tickets_first_class: int, num_of_available_tickets_second_class: int,
                           price_first_class: float , price_second_class: float, from_city: str, to_city: str):
        """
        It creates a new view flight object and adds it to the database.  """
        try:
            view_flight = ViewFlight(flight_id=flight_id, departure_time=departure_time,arrival_time=arrival_time,
                                     airline=airline, num_of_seats=num_of_seats,
                                     num_of_available_tickets_first_class=num_of_available_tickets_first_class,
                                     num_of_available_tickets_second_class=num_of_available_tickets_second_class,
                                     price_first_class=price_first_class, price_second_class=price_second_class,
                                     from_city=from_city, to_city=to_city)
            self.db.add(view_flight)
            self.db.commit()
            self.db.refresh(view_flight)
            return view_flight
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    def sort_view_flight_by_price(self):
        """
        It sorts the view_flights by price_second_class.
        @returns A list of all the flights in the database, sorted by price.
        """
        view_flights = self.db.query(ViewFlight).order_by(ViewFlight.price_second_class).all()
        return view_flights


    def delete_view_flight(self):
        """
        It deletes all the rows in the ViewFlight table
        @returns True
        """
        try:
            view_flight = self.db.query(ViewFlight).delete()
            self.db.commit()
            return True
        except Exception as e:
            raise e