from fastapi import APIRouter, Depends
from app.tickets.controller import TicketController
from app.tickets.schemas import TicketSchema, TicketSchemaIn
from app.users.controller.user_auth_controller import JWTSuperUserBearer, JWTClassicUserBearer

ticket_router = APIRouter(tags=["Tickets"], prefix="/api/tickets")


@ticket_router.post("/create-new-ticket", response_model=TicketSchema, dependencies=[Depends(JWTSuperUserBearer())])
def create_new_ticket(ticket: TicketSchemaIn):
    """
    It creates a new ticket
    @param {TicketSchemaIn} ticket - TicketSchemaIn
    @returns A ticket object
    """
    return TicketController.create_new_ticket(class_number=ticket.class_number, ticket_price=ticket.ticket_price,flight_id=ticket.flight_id, is_it_reserved=ticket.is_it_reserved)

@ticket_router.post("/create-n-tickets", response_model=list[TicketSchema], dependencies=[Depends(JWTSuperUserBearer())])
def create_n_tickets(number_of_tickets: int,ticket: TicketSchemaIn):
    """
    It creates n tickets for a flight.
    @param {int} number_of_tickets - int
    @param {TicketSchemaIn} ticket - TicketSchemaIn
    @returns A list of tickets
    """
    return TicketController.create_n_tickets(number_of_tickets=number_of_tickets,class_number=ticket.class_number, ticket_price=ticket.ticket_price,flight_id=ticket.flight_id, is_it_reserved=ticket.is_it_reserved)

@ticket_router.post("/create-all-tickets-for-flight", response_model=list[TicketSchema], dependencies=[Depends(JWTSuperUserBearer())])
def create_all_tickets_for_flight(flight_id: str,ticket_price: str):
    """
    Create all tickets for flight by flight id
    @param {str} flight_id - The id of the flight you want to create tickets for.
    @param {str} ticket_price - The price of the ticket
    @returns A list of all the tickets for a flight
    """
    return TicketController.create_all_tickets_for_flight_by_flight_id(flight_id=flight_id, ticket_price=ticket_price)


@ticket_router.get("/get-all-tickets", response_model=list[TicketSchema], dependencies=[Depends(JWTSuperUserBearer())])
def get_all_tickets():
    """
    It returns a list of all the tickets in the database
    @returns A list of all the tickets in the database.
    """
    tickets = TicketController.get_all_tickets()
    return tickets

@ticket_router.get("/get-ticket-by-id", response_model=TicketSchema, dependencies=[Depends(JWTSuperUserBearer())])
def get_ticket_by_id(ticket_id: str):
    """
    `get_ticket_by_id` returns a ticket object given a ticket id
    @param {str} ticket_id - The ID of the ticket you want to get.
    @returns A ticket object
    """
    return TicketController.get_ticket_by_id(ticket_id)


@ticket_router.delete("/delete-flight", dependencies=[Depends(JWTSuperUserBearer())])
def delete_ticket_by_id(ticket_id: str):
    """
    `Delete a ticket by id.`
    @param {str} ticket_id - str
    @returns The ticket_id of the ticket that was deleted.
    """
    return TicketController.delete_ticket_by_id(ticket_id)
