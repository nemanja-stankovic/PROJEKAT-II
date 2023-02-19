from app.db import SessionLocal
from app.tickets.repositories import TicketRepository



class TicketService:

    @staticmethod
    def create_new_ticket(class_number, ticket_price, flight_id, is_it_reserved):
        try:
            with SessionLocal() as db:
                repository = TicketRepository(db)
                return repository.create_ticket(class_number, ticket_price, flight_id, is_it_reserved)
        except Exception as e:
            raise e

    @staticmethod
    def read_all_tickets():
        try:
            with SessionLocal() as db:
                repository = TicketRepository(db)
                return repository.read_all_tickets()
        except Exception as e:
            raise e

    @staticmethod
    def read_ticket_by_id(ticket_id):
        try:
            with SessionLocal() as db:
                repository = TicketRepository(db)
                return repository.read_ticket_by_id(ticket_id)
        except Exception as e:
            raise e

    @staticmethod
    def delete_ticket_by_id(ticket_id):
        try:
            with SessionLocal() as db:
                repository = TicketRepository(db)
                return repository.delete_ticket(ticket_id)
        except Exception as e:
            raise e