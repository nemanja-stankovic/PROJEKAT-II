from app.db import SessionLocal
from app.reservations.repositories import ReservationRepository


class ReservationService:

    @staticmethod
    def create_new_reservation(ticket_id: str, user_id: str):
        try:
            with SessionLocal() as db:
                repository = ReservationRepository(db)
                return repository.create_reservation(ticket_id, user_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_all_reservations():
        try:
            with SessionLocal() as db:
                repository = ReservationRepository(db)
                return repository.read_all_reservations()
        except Exception as e:
            raise e

    @staticmethod
    def read_reservation_by_id(reservation_id):
        try:
            with SessionLocal() as db:
                repository = ReservationRepository(db)
                return repository.read_reservation_by_id(reservation_id)
        except Exception as e:
            raise e


    @staticmethod
    def delete_reservation_by_id(reservation_id):
        try:
            with SessionLocal() as db:
                repository = ReservationRepository(db)
                return repository.delete_reservation(reservation_id)
        except Exception as e:
            raise e
