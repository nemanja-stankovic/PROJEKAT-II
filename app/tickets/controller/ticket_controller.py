from app.tickets.exceptions import TicketExceptionCode, TicketNotFoundException
from app.tickets.servicies import TicketService
from fastapi import HTTPException, Response
from app.tickets.exceptions import TicketNotFoundException
from app.flights.servicies import FlightService


class TicketController:

    @staticmethod
    def create_new_ticket(class_number, ticket_price, flight_id, is_it_reserved):
        """
        It creates a new ticket for a flight
        @param class_number - The class number of the ticket.
        @param ticket_price - The price of the ticket
        @param flight_id - The id of the flight that the ticket is for.
        @param is_it_reserved - True or False
        @returns Ticket object
        """
        try:
            flight = FlightService.read_flight_by_id(flight_id)
            number_of_seats = flight.num_of_seats
            tickets = TicketService.read_tickets_by_flight_id(flight_id)
            if number_of_seats > len(tickets):
                ticket = TicketService.create_new_ticket(class_number, ticket_price, flight_id, is_it_reserved)
                return ticket
            else:
                raise HTTPException(status_code=500, detail=f"All tickets are added to this flight. Maximum number of seats {number_of_seats}")
        except TicketExceptionCode as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def create_n_tickets(number_of_tickets,class_number, ticket_price, flight_id, is_it_reserved):
        """
        It creates a list of tickets, and if the number of tickets is less than the number of seats, it adds the tickets to
        the list
        @param number_of_tickets - The number of tickets you want to create
        @param class_number - 1,2,3
        @param ticket_price - The price of the ticket
        @param flight_id - The id of the flight that the ticket is for
        @param is_it_reserved - True or False
        @returns A list of tickets
        """
        try:
            number_of_added = 0
            list_of_tickets = []
            for i in range(number_of_tickets):
                ticket = TicketController.create_new_ticket(class_number, ticket_price, flight_id, is_it_reserved)
                list_of_tickets.append(ticket)
                flight = FlightService.read_flight_by_id(flight_id)
                number_of_seats = flight.num_of_seats
                tickets = TicketService.read_tickets_by_flight_id(flight_id)
                if number_of_seats > len(tickets):
                    number_of_added +=1
                    continue
                else:
                    break
            return list_of_tickets
        except TicketExceptionCode as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            if number_of_added == 0:
                raise HTTPException(status_code=400, detail=f"Succesifully added {number_of_added} tickets out of {number_of_tickets} number_of_tickets")
            else:
                raise HTTPException(status_code=200,
                                    detail=f"Succesfully added {number_of_added} tickets out of {number_of_tickets} number_of_tickets")

    @staticmethod
    def create_all_tickets_for_flight_by_flight_id(flight_id, ticket_price):
        """
        It creates all the tickets for a flight by flight id
        @param flight_id - the id of the flight that we want to create tickets for
        @param ticket_price - the price of the ticket
        @returns A list of tickets
        """
        try:
            flight = FlightService.read_flight_by_id(flight_id)
            num_of_seats = flight.num_of_seats
            tickets = TicketController.create_n_tickets(number_of_tickets=num_of_seats,class_number=2,ticket_price=ticket_price,flight_id=flight_id,is_it_reserved=False)
            if flight is not None:
                return tickets
            else:
                raise HTTPException(status_code=500, detail=f"flight with id {flight_id} not found")
        except TicketNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    @staticmethod
    def get_all_tickets():
        """
        It returns all the tickets in the database
        @returns A list of all tickets
        """
        try:
            tickets = TicketService.read_all_tickets()
            return tickets
        except TicketNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))


    @staticmethod
    def search_tickets_by_flight_id(flight_id):
        """
        It takes a flight_id as an argument and returns a list of tickets that have that flight_id
        @param flight_id - The flight id of the flight whose tickets are to be searched.
        @returns A list of tickets
        """
        try:
            tickets= TicketService.read_ticket_by_flight_id(flight_id)
            return tickets
        except TicketNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_ticket_by_id(ticket_id: str):
        """
        > This function will return a ticket object if the ticket exists, otherwise it will return an error
        @param {str} ticket_id - The id of the ticket to be retrieved.
        @returns A ticket object
        """
        try:
            ticket = TicketService.read_ticket_by_id(ticket_id)
            return ticket
        except TicketNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))


    @staticmethod
    def delete_ticket_by_id(ticket_id: str):
        """
        It deletes a ticket by ID.
        @param {str} ticket_id - str - this is the ID of the ticket we want to delete.
        @returns Response object
        """
        try:
            TicketService.delete_ticket_by_id(ticket_id)
            return Response(content=f"Ticket with provided ID: {ticket_id} deleted.", status_code=200)
        except TicketNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_number_of_available_tickets_by_flight_id(flight_id: str):
        """
        It returns the number of available tickets for a given flight id
        @param {str} flight_id - str
        @returns The number of available tickets for a flight
        """
        try:
            number_of_tickets = TicketService.read_number_of_available_tickets_by_flight_id(flight_id)
            if number_of_tickets:
                return number_of_tickets
            else:
                raise HTTPException(status_code=400, detail="There is no available ticket for this flight")
        except TicketNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def update_ticket_price(flight_id: str, class_number: int, price: float):
        """
        It updates the ticket price for a given flight id, class number and price.
        @param {str} flight_id - str
        @param {int} class_number - 1 for first class, 2 for business class, 3 for economy class
        @param {float} price - float
        """
        try:
            tickets = TicketService.update_ticket_price(flight_id, class_number, price)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
