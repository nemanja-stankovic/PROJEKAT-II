from app.reservations.exceptions import ReservationExceptionCode, ReservationNotFoundException
from fastapi import HTTPException, Response
from app.reservations.servicies import ReservationService


class ReservationController:

    @staticmethod
    def create_new_reservation(ticket_id: str, user_id: str):
        try:
            reservation = ReservationService.create_new_reservation(ticket_id, user_id)

            return reservation
        except ReservationExceptionCode as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_reservations():
        reservations = ReservationService.read_all_reservations()
        return reservations


    @staticmethod
    def get_reservation_by_id(reservation_id: str):
        try:
            reservation = ReservationService.read_reservation_by_id(reservation_id)
            return reservation
        except ReservationNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))


    @staticmethod
    def delete_reservation_by_id(reservation_id: str):
        try:
            ReservationService.delete_reservation_by_id(reservation_id)
            return Response(content=f"Reservation with provided ID: {reservation_id} deleted.", status_code=200)
        except ReservationNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))


