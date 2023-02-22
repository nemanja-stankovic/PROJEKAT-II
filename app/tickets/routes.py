from fastapi import APIRouter
from app.tickets.controller import TicketController
from app.tickets.schemas import TicketSchema, TicketSchemaIn


ticket_router = APIRouter(tags=["Tickets"], prefix="/api/tickets")


@ticket_router.post("/create-new-ticket", response_model=TicketSchema)
def create_new_ticket(ticket: TicketSchemaIn):
    return TicketController.create_new_ticket(class_number=ticket.class_number, ticket_price=ticket.ticket_price,flight_id=ticket.flight_id, is_it_reserved=ticket.is_it_reserved)

@ticket_router.post("/create-n-tickets", response_model=list[TicketSchema])
def create_n_tickets(number_of_tickets: int,ticket: TicketSchemaIn):
    return TicketController.create_n_tickets(number_of_tickets=number_of_tickets,class_number=ticket.class_number, ticket_price=ticket.ticket_price,flight_id=ticket.flight_id, is_it_reserved=ticket.is_it_reserved)

@ticket_router.post("/create-all-tickets-for-flight", response_model=list[TicketSchema])
def create_all_tickets_for_flight(flight_id: str,ticket_price: str):
    return TicketController.create_all_tickets_for_flight_by_flight_id(flight_id=flight_id, ticket_price=ticket_price)


@ticket_router.get("/get-all-tickets", response_model=list[TicketSchema])
def get_all_tickets():
    tickets = TicketController.get_all_tickets()
    return tickets

@ticket_router.get("/get-ticket-by-id", response_model=TicketSchema)
def get_ticket_by_id(ticket_id: str):
    return TicketController.get_ticket_by_id(ticket_id)


@ticket_router.delete("/delete-flight")
def delete_ticket_by_id(ticket_id: str):
    return TicketController.delete_ticket_by_id(ticket_id)
