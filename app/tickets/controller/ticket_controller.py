from app.tickets.exceptions import TicketExceptionCode, TicketNotFoundException
from app.tickets.servicies import TicketService
from fastapi import HTTPException, Response
from app.tickets.exceptions import TicketNotFoundException


class TicketController:

    @staticmethod
    def create_new_ticket(class_number, ticket_price, flight_id, is_it_reserved):
        try:
            ticket = TicketService.create_new_ticket(class_number, ticket_price, flight_id, is_it_reserved)
            return ticket
        except TicketExceptionCode as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_tickets():
        tickets = TicketService.read_all_tickets()
        return tickets

    @staticmethod
    def search_tickets_by_flight_id(flight_id):
        tickets = TicketService.read_all_tickets()
        tickets_list=[]
        for ticket in tickets:
            if flight_id == ticket.flight_id:
                tickets_list.append(ticket)
        return tickets_list


    @staticmethod
    def get_ticket_by_id(ticket_id: str):
        try:
            ticket = TicketService.read_ticket_by_id(ticket_id)
            return ticket
        except TicketNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))


    @staticmethod
    def delete_ticket_by_id(ticket_id: str):
        try:
            TicketService.delete_ticket_by_id(ticket_id)
            return Response(content=f"Ticket with provided ID: {ticket_id} deleted.", status_code=200)
        except TicketNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
