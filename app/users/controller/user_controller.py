from sqlalchemy.exc import IntegrityError
from app.users.servicies import UserServices
from app.users.servicies.user_auth_handler_service import signClassicUserJWT, signSuperUserJWT
from fastapi import HTTPException, Response
from app.users.exceptions import UserInvalidePassword
from app.flights.servicies import FlightService
from app.tickets.servicies import TicketService

class UserController:
    @staticmethod
    def create_user(email, password):
        try:
            user = UserServices.create_user(email, password)
            return user
        except IntegrityError as e:
            raise HTTPException(status_code=400, detail=f"User with provided email - {email} already exists.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def create_super_user(email, password):
        try:
            user = UserServices.create_super_user(email, password)
            return user
        except IntegrityError as e:
            raise HTTPException(status_code=400, detail=f"User with provided email - {email} already exists.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def login_user(email, password):
        try:

            user = UserServices.login_user(email, password)
            user_id = UserServices.read_user_id_by_email(email)
            user = UserServices.update_user_is_active(user_id, is_active=True)
            if user.is_superuser:
                return signSuperUserJWT(user_id)
            return signClassicUserJWT(user.id)
        except UserInvalidePassword as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def logout_user(email):
        try:
            user_id = UserServices.read_user_id_by_email(email)
            return UserServices.update_user_is_active(user_id, is_active=False)

        except UserInvalidePassword as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_user_by_id(user_id: str):
        user = UserServices.get_user_by_id(user_id)
        if user:
            return user
        else:
            raise HTTPException(status_code=400, detail=f"user with provided id {user_id} does not exist")

    @staticmethod
    def get_all_users():
        users = UserServices.get_all_users()
        return users

    @staticmethod
    def delete_user_by_id(user_id: str):
        try:
            UserServices.delete_user_by_id(user_id)
            return Response(content=f"User with id - {user_id} is deleted")
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def update_user_is_active(user_id: str, is_active: bool):
        try:
            user = UserServices.update_user_is_active(user_id, is_active)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def reserve_flight_by_flight_id_and_class_number(flight_id, class_number):
        try:
            number_of_available_tickets = TicketService.read_number_of_available_tickets_by_flight_id(flight_id)
            if number_of_available_tickets == 0:
                raise HTTPException(status_code=400, detail="There is no available ticket for this flight")
            else:
                tickets = TicketService.read_tickets_by_flight_id(flight_id)
                list_ticket = []
                for ticket in tickets:
                    ticket_id = ticket.ticket_id
                    if (ticket.is_it_reserved == False):
                        list_ticket.append(ticket)
                        TicketService.update_is_it_reserved(ticket_id)
                return list_ticket[0]
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
