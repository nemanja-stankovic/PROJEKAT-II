from fastapi import APIRouter
from app.reservations.schemas import ReservationSchema, ReservationSchemaIn
from app.reservations.controller import ReservationController


reservation_router = APIRouter(tags=["Reservations"], prefix="/api/reservations")

@reservation_router.post("/create-new-reservation")
def create_new_reservation(reservation: ReservationSchemaIn):
    """
    > Create a new reservation for a ticket
    @param {ReservationSchemaIn} reservation - ReservationSchemaIn
    @returns A reservation object
    """
    return ReservationController.create_new_reservation(ticket_id=reservation.ticket_id, user_id=reservation.user_id)

@reservation_router.get("/get-all-reservations", response_model=list[ReservationSchema])
def get_all_reservations():
    """
    This function returns a list of all reservations in the database
    @returns A list of all reservations
    """
    reservations = ReservationController.get_all_reservations()
    return reservations

@reservation_router.get("/get-reservation-by-id", response_model=ReservationSchema)
def get_reservation_by_id(reservation_id: str):
    """
    `Get a reservation by its id.`
    @param {str} reservation_id - The id of the reservation you want to get.
    @returns A reservation object
    """
    return ReservationController.get_reservation_by_id(reservation_id)

@reservation_router.delete("/delete-reservation")
def delete_reservation(reservation_id: str):
    """
    `Delete a reservation by id.`
    @param {str} reservation_id - The id of the reservation to delete.
    @returns A reservation object
    """
    return ReservationController.delete_reservation_by_id(reservation_id)
