"""It creates a new reservation, reads all reservations, reads a reservation by id, and deletes a reservation by id
"""
from app.db import SessionLocal
from app.reservations.repositories import ReservationRepository



class ReservationService:
    """"This class is responsible for handling reservations"""
    @staticmethod
    def create_new_reservation(ticket_id: str, user_id: str):
        """
        It creates a new reservation for a ticket and a user
        @param {str} ticket_id - str
        @param {str} user_id - str - the user id of the user who is making the reservation
        @returns A reservation object
        """
        try:
            with SessionLocal() as db:
                repository = ReservationRepository(db)
                reservations = repository.read_all_reservations()
                ticket_ids = []
                for reservation in reservations:
                    ticket_id_b = reservation.ticket_id
                    ticket_ids.append(ticket_id_b)
                if ticket_id not in ticket_ids:
                    return repository.create_reservation(ticket_id, user_id)
                raise Exception("Ticket is not available")
        except Exception as e:
            raise e

    @staticmethod
    def read_all_reservations():
        """
        It creates a database session, creates a repository, and then calls the repository's read_all_reservations()
        function
        @returns A list of all reservations in the database.
        """
        try:
            with SessionLocal() as db:
                repository = ReservationRepository(db)
                return repository.read_all_reservations()
        except Exception as e:
            raise e

    @staticmethod
    def read_reservation_by_id(reservation_id):
        """
        It reads a reservation by id
        @param reservation_id - The id of the reservation to be read.
        @returns A reservation object
        """
        try:
            with SessionLocal() as db:
                repository = ReservationRepository(db)
                return repository.read_reservation_by_id(reservation_id)
        except Exception as e:
            raise e


    @staticmethod
    def delete_reservation_by_id(reservation_id):
        """
        It deletes a reservation by id
        @param reservation_id - The id of the reservation to be deleted.
        @returns The reservation object that was deleted.
        """
        try:
            with SessionLocal() as db:
                repository = ReservationRepository(db)
                return repository.delete_reservation(reservation_id)
        except Exception as e:
            raise e
