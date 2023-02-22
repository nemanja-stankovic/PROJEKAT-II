# It's a class that contains methods that perform CRUD operations on the Ticket table in the database
from app.tickets.models import Ticket
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.tickets.exceptions import TicketNotFoundException


class TicketRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_ticket(self, class_number, ticket_price, flight_id, is_it_reserved):
        try:
            ticket = Ticket(class_number=class_number,ticket_price=ticket_price,flight_id=flight_id, is_it_reserved=is_it_reserved)
            self.db.add(ticket)
            self.db.commit()
            self.db.refresh(ticket)
            return ticket
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    def read_all_tickets(self):
        tickets = self.db.query(Ticket).all()
        return tickets

    def read_ticket_by_id(self, ticket_id: str):
        ticket = self.db.query(Ticket).filter(Ticket.ticket_id == ticket_id).first()
        if ticket is None:
            raise TicketNotFoundException(f"Ticket with provided ID: {ticket_id} not found.", 400)
        return ticket

    def read_ticket_by_flight_id(self, flight_id: str):
        tickets = self.db.query(Ticket).filter(Ticket.flight_id == flight_id).all()
        return tickets
    def read_tickets_by_class(self, class_number: int):
        tickets = self.db.query(Ticket).filter(Ticket.class_number == class_number).all()
        return tickets

    def update_price_for_ticket(self, flight_id: str, class_number: int,price: float):
        tickets = self.db.query(Ticket).filter(Ticket.class_number == class_number, Ticket.flight_id == flight_id).all()
        for ticket in tickets:
            ticket.ticket_price = price
            self.db.add(ticket)
            self.db.commit()
            self.db.refresh(ticket)
        return tickets
    def update_is_it_reserved(self, ticket_id: str):
        ticket = self.db.query(Ticket).filter(Ticket.ticket_id == ticket_id).first()
        ticket.is_it_reserved = True
        self.db.add(ticket)
        self.db.commit()
        self.db.refresh(ticket)
        return ticket

    # def read_price_by_class_and_flight_id(self, class_number: int, flight_id):
    #     ticket = self.db.query(Ticket).filter(Ticket.class_number == class_number & Ticket.flight_id == flight_id).first()
    #     if ticket is None:
    #         raise TicketNotFoundException(f"Price with provided class_number: {class_number} and flight_id: {flight_id}not found.", 400)
    #     return ticket.ticket_price

    def delete_ticket(self, ticket_id: str):
        try:
            ticket = self.db.query(Ticket).filter(Ticket.ticket_id == ticket_id).first()
            if ticket is None:
                raise TicketNotFoundException(f"Ticket with provided ID: {ticket_id} not found.", 400)
            self.db.delete(ticket)
            self.db.commit()
            return True
        except Exception as e:
            raise e
