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