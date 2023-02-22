from app.db import SessionLocal
from app.tickets.repositories import TicketRepository
from app.flights.repositories import FlightRepository

def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

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
    def create_n_tickets(number_of_tickets,class_number, ticket_price, flight_id, is_it_reserved):
        try:
            with SessionLocal() as db:
                ticket_repository = TicketRepository(db)
                flight_repository = FlightRepository(db)
                list_of_tickets = []
                for i in range(number_of_tickets):
                    ticket = ticket_repository.create_ticket(class_number, ticket_price, flight_id, is_it_reserved)
                    list_of_tickets.append(ticket)
                    flight = flight_repository.read_flight_by_id(flight_id)
                    number_of_seats = flight.num_of_seats
                    tickets = TicketService.read_tickets_by_flight_id(flight_id)
                return ticket
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
    def read_tickets_by_flight_id(flight_id):
        try:
            with SessionLocal() as db:
                repository = TicketRepository(db)
                return repository.read_ticket_by_flight_id(flight_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_price_by_class_and_flight_id(flight_class, flight_id):
        try:
            with SessionLocal() as db:
                repository = TicketRepository(db)
                tickets = repository.read_tickets_by_class(flight_class)
                list_of_tickets = []
                for ticket in tickets:
                    if ticket.flight_id == flight_id:
                        price = ticket.ticket_price
                        list_of_tickets.append(price)
                if len(list_of_tickets) > 0:
                    return price
                else:
                    return 0

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

    @staticmethod
    def read_number_of_available_tickets_by_flight_id(flight_id):
        try:
            with SessionLocal() as db:
                repository = TicketRepository(db)
                tickets = repository.read_ticket_by_flight_id(flight_id)
                if bool(tickets) == True:
                    return len(tickets)
        except Exception as e:
            raise e

    @staticmethod
    def read_number_of_available_tickets_by_flight_id_and_class_number(flight_id, class_number):
        try:
            with SessionLocal() as db:
                repository = TicketRepository(db)
                tickets_1 = repository.read_tickets_by_class(class_number)
                tickets_2 = repository.read_ticket_by_flight_id(flight_id)
                tickets = intersection(tickets_1,tickets_2)

                number_of_tickets=len(tickets)
                return number_of_tickets
        except Exception as e:
            raise e

    @staticmethod
    def update_ticket_price(flight_id, class_number, price):
        try:
            with SessionLocal() as db:
                repository = TicketRepository(db)
                tickets = repository.update_price_for_ticket(flight_id, class_number, price)
                return tickets
        except Exception as e:
            raise e
    @staticmethod
    def update_is_it_reserved(ticket_id):
        try:
            with SessionLocal() as db:
                repository = TicketRepository(db)
                ticket = repository.update_is_it_reserved(ticket_id)
                return ticket
        except Exception as e:
            raise e