"""It's a class that contains methods that perform CRUD operations on the Ticket table in the database"""
from app.tickets.models import Ticket
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.tickets.exceptions import TicketNotFoundException


class TicketRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_ticket(self, class_number, ticket_price, flight_id, is_it_reserved):
        """
        It creates a ticket object and adds it to the database
        @param class_number - The class number of the ticket.
        @param ticket_price - The price of the ticket
        @param flight_id - The id of the flight that the ticket is for.
        @param is_it_reserved - This is a boolean value that is set to False by default.
        @returns The ticket object is being returned.
        """
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
        """
        It returns all the tickets in the database
        @returns A list of all the tickets in the database.
        """
        tickets = self.db.query(Ticket).all()
        return tickets

    def read_ticket_by_id(self, ticket_id: str):
        """
        It takes a ticket_id as a string, and returns a ticket object from the database
        @param {str} ticket_id - str
        @returns Ticket object
        """
        ticket = self.db.query(Ticket).filter(Ticket.ticket_id == ticket_id).first()
        if ticket is None:
            raise TicketNotFoundException(f"Ticket with provided ID: {ticket_id} not found.", 400)
        return ticket

    def read_ticket_by_flight_id(self, flight_id: str):
        """
        It returns all the tickets for a given flight
        @param {str} flight_id - str
        @returns A list of tickets
        """
        try:
            tickets = self.db.query(Ticket).filter(Ticket.flight_id == flight_id).all()
            if bool(tickets) is not False:
                return tickets
            raise TicketNotFoundException(code=400, message="There is no ticket for that flight")
        except Exception as e:
            raise e

    def read_tickets_by_class(self, class_number: int):
        """
        This function returns a list of all tickets in the database that have a class number equal to the class number
        passed in as a parameter
        @param {int} class_number - int
        @returns A list of tickets
        """
        tickets = self.db.query(Ticket).filter(Ticket.class_number == class_number).all()
        return tickets

    def update_price_for_ticket(self, flight_id: str, class_number: int,price: float):
        """
        It updates the price of all tickets for a given flight and class number
        @param {str} flight_id - str
        @param {int} class_number - int
        @param {float} price - float
        @returns A list of tickets
        """
        tickets = self.db.query(Ticket).filter(Ticket.class_number == class_number, Ticket.flight_id == flight_id).all()
        for ticket in tickets:
            ticket.ticket_price = price
            self.db.add(ticket)
            self.db.commit()
            self.db.refresh(ticket)
        return tickets
    def update_is_it_reserved(self, ticket_id: str):
        """
        It updates the is_it_reserved column in the Ticket table to True for the ticket with the ticket_id that is passed in
        as an argument
        @param {str} ticket_id - str
        @returns The ticket object
        """
        ticket = self.db.query(Ticket).filter(Ticket.ticket_id == ticket_id).first()
        ticket.is_it_reserved = True
        self.db.add(ticket)
        self.db.commit()
        self.db.refresh(ticket)
        return ticket


    def delete_ticket(self, ticket_id: str):
        """
        It deletes a ticket from the database
        @param {str} ticket_id - The ID of the ticket to be deleted.
        @returns True
        """
        try:
            ticket = self.db.query(Ticket).filter(Ticket.ticket_id == ticket_id).first()
            if ticket is None:
                raise TicketNotFoundException(f"Ticket with provided ID: {ticket_id} not found.", 400)
            self.db.delete(ticket)
            self.db.commit()
            return True
        except Exception as e:
            raise e
