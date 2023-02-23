from app.db import SessionLocal
from app.tickets.repositories import TicketRepository
from app.flights.repositories import FlightRepository

def intersection(lst1, lst2):
    """
    It takes two lists, converts them to sets, takes the intersection of the sets, and then converts the result back to a
    list
    @param lst1 - The first list.
    @param lst2 - The list to be searched for elements in lst1.
    @returns The intersection of the two lists.
    """
    return list(set(lst1) & set(lst2))


class TicketService:
    """This class is responsible for providing ticket services"""
    @staticmethod
    def create_new_ticket(class_number, ticket_price, flight_id, is_it_reserved):
        """
        It creates a new ticket in the database
        @param class_number - The class number of the ticket.
        @param ticket_price - The price of the ticket
        @param flight_id - The id of the flight that the ticket is for.
        @param is_it_reserved - True or False
        @returns The ticket object
        """
        try:
            with SessionLocal() as db:
                repository = TicketRepository(db)
                return repository.create_ticket(class_number, ticket_price, flight_id, is_it_reserved)
        except Exception as e:
            raise e

    @staticmethod
    def create_n_tickets(number_of_tickets,class_number, ticket_price, flight_id, is_it_reserved):
        """
        It creates a list of tickets for a flight
        @param number_of_tickets - The number of tickets you want to create
        @param class_number - 1,2,3
        @param ticket_price - The price of the ticket
        @param flight_id - The id of the flight that the ticket is for
        @param is_it_reserved - True or False
        @returns A list of tickets
        """
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
        """
        It creates a database session, creates a repository, and then calls the repository's read_all_tickets() function
        @returns A list of all tickets in the database.
        """
        try:
            with SessionLocal() as db:
                repository = TicketRepository(db)
                return repository.read_all_tickets()
        except Exception as e:
            raise e

    @staticmethod
    def read_ticket_by_id(ticket_id):
        """
        It reads a ticket by id
        @param ticket_id - The id of the ticket to be read.
        @returns A ticket object
        """
        try:
            with SessionLocal() as db:
                repository = TicketRepository(db)
                return repository.read_ticket_by_id(ticket_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_tickets_by_flight_id(flight_id):
        """
        It reads all the tickets for a given flight_id
        @param flight_id - The id of the flight you want to get the tickets for.
        @returns A list of tickets
        """
        try:
            with SessionLocal() as db:
                repository = TicketRepository(db)
                return repository.read_ticket_by_flight_id(flight_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_price_by_class_and_flight_id(flight_class, flight_id):
        """
        It reads the price of a ticket by class and flight id
        @param flight_class - economy, business, first
        @param flight_id - The id of the flight
        @returns The price of the ticket
        """
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
        """
        It deletes a ticket from the database by its id
        @param ticket_id - The id of the ticket to be deleted.
        @returns The ticket_id of the ticket that was deleted.
        """
        try:
            with SessionLocal() as db:
                repository = TicketRepository(db)
                return repository.delete_ticket(ticket_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_number_of_available_tickets_by_flight_id(flight_id):
        """
        It returns the number of available tickets for a given flight
        @param flight_id - The id of the flight you want to get the number of available tickets for.
        @returns The number of tickets available for a flight.
        """
        try:
            with SessionLocal() as db:
                repository = TicketRepository(db)
                tickets = repository.read_ticket_by_flight_id(flight_id)
                ticket_list = []
                for ticket in tickets:
                    if ticket.is_it_reserved == False:
                        ticket_list.append(ticket)
                return len(tickets)
        except Exception as e:
            raise e

    @staticmethod
    def read_number_of_available_tickets_by_flight_id_and_class_number(flight_id, class_number):
        """
        It returns the number of available tickets for a given flight and class
        @param flight_id - the id of the flight
        @param class_number - 1, 2, 3
        @returns The number of tickets available for a flight and class
        """
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
        """
        It updates the price of a ticket for a given flight and class number
        @param flight_id - The id of the flight you want to update the ticket price for.
        @param class_number - 1, 2, 3
        @param price - The new price of the ticket
        @returns A list of tickets
        """
        try:
            with SessionLocal() as db:
                repository = TicketRepository(db)
                tickets = repository.update_price_for_ticket(flight_id, class_number, price)
                return tickets
        except Exception as e:
            raise e
    @staticmethod
    def update_is_it_reserved(ticket_id):
        """
        It updates the is_it_reserved column in the ticket table to True
        @param ticket_id - The id of the ticket that you want to update.
        @returns Ticket object
        """
        try:
            with SessionLocal() as db:
                repository = TicketRepository(db)
                ticket = repository.update_is_it_reserved(ticket_id)
                return ticket
        except Exception as e:
            raise e