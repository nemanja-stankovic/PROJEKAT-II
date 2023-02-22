from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.reservations.models import Reservation
from app.reservations.exceptions import ReservationNotFoundException


class ReservationRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_reservation(self, ticket_id, user_id):
        """
        It creates a new reservation for a ticket and user
        @param ticket_id - The id of the ticket that is being reserved.
        @param user_id - The id of the user who is making the reservation.
        @returns A reservation object
        """
        try:
            reservation = Reservation(ticket_id=ticket_id, user_id=user_id)
            self.db.add(reservation)
            self.db.commit()
            self.db.refresh(reservation)
            return reservation
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    def read_all_reservations(self):
        """
        It returns all the reservations in the database
        @returns A list of all reservations in the database.
        """
        reservations = self.db.query(Reservation).all()
        return reservations

    def read_reservation_by_id(self, reservation_id: str):
        """
        It returns a reservation object from the database if it exists, otherwise it raises an exception
        @param {str} reservation_id - The ID of the reservation to be read.
        @returns The reservation object is being returned.
        """
        reservation = self.db.query(Reservation).filter(Reservation.reservation_id == reservation_id).first()
        if reservation is None:
            raise ReservationNotFoundException(f"Flight with provided ID: {reservation_id} not found.", 400)
        return reservation

    def delete_reservation(self, reservation_id: str):
        """
        It deletes a reservation from the database
        @param {str} reservation_id - The ID of the reservation to be deleted.
        @returns True
        """
        try:
            reservation = self.db.query(Reservation).filter(Reservation.reservation_id == reservation_id).first()
            if reservation is None:
                raise ReservationNotFoundException(f"Reservation with provided ID: {reservation_id} not found.", 400)
            self.db.delete(reservation)
            self.db.commit()
            return True
        except Exception as e:
            raise e
