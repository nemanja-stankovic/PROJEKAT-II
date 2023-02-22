"""It contains all the methods that are used to interact with the reservations database"""
from app.reservations.exceptions import ReservationExceptionCode, ReservationNotFoundException
from fastapi import HTTPException, Response
from app.reservations.servicies import ReservationService
from app.tickets.servicies import TicketService


class ReservationController:
    """This class is responsible for handling all reservation related requests"""
    @staticmethod
    def create_new_reservation(ticket_id: str, user_id: str):
        """
        It creates a new reservation
        @param {str} ticket_id - str, user_id: str
        @param {str} user_id - str - the user id of the user who is making the reservation
        @returns A reservation object
        """
        try:

            reservation = ReservationService.create_new_reservation(ticket_id, user_id)
            return reservation
        except ReservationExceptionCode as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_all_reservations():
        """
        It returns a list of all reservations in the database
        @returns A list of all reservations
        """
        reservations = ReservationService.read_all_reservations()
        return reservations


    @staticmethod
    def get_reservation_by_id(reservation_id: str):
        """
        > This function gets a reservation by id
        @param {str} reservation_id - The id of the reservation to be retrieved.
        @returns A reservation object
        """
        try:
            reservation = ReservationService.read_reservation_by_id(reservation_id)
            return reservation
        except ReservationNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e


    @staticmethod
    def delete_reservation_by_id(reservation_id: str):
        """
        It deletes a reservation by id.
        @param {str} reservation_id - str - the ID of the reservation to be deleted
        @returns Response object
        """
        try:
            ReservationService.delete_reservation_by_id(reservation_id)
            return Response(content=f"Reservation with provided ID: {reservation_id} deleted.", status_code=200)
        except ReservationNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e
