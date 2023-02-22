from fastapi import APIRouter
from app.reservations.schemas import ReservationSchema, ReservationSchemaIn
from app.reservations.controller import ReservationController


reservation_router = APIRouter(tags=["Reservations"], prefix="/api/reservations")

@reservation_router.post("/create-new-reservation")
def create_new_reservation(reservation: ReservationSchemaIn):
    return ReservationController.create_new_reservation(ticket_id=reservation.ticket_id, user_id=reservation.user_id)

@reservation_router.get("/get-all-reservations", response_model=list[ReservationSchema])
def get_all_reservations():
    reservations = ReservationController.get_all_reservations()
    return reservations

@reservation_router.get("/get-reservation-by-id", response_model=ReservationSchema)
def get_reservation_by_id(reservation_id: str):
    return ReservationController.get_reservation_by_id(reservation_id)

@reservation_router.delete("/delete-reservation")
def delete_reservation(reservation_id: str):
    return ReservationController.delete_reservation_by_id(reservation_id)

