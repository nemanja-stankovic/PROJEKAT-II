from sqlalchemy.exc import IntegrityError
from app.users.servicies import UserServices
from app.users.servicies.user_auth_handler_service import signClassicUserJWT, signSuperUserJWT
from fastapi import HTTPException, Response
from app.users.exceptions import UserInvalidePassword
from app.flights.servicies import FlightService
from app.tickets.servicies import TicketService
from app.reservations.servicies import ReservationService
class UserController:
    @staticmethod
    def create_user(email, password):
        """
        It creates a user with the provided email and password
        @param email - The email of the user.
        @param password - The password to be hashed.
        @returns The user object is being returned.
        """
        try:
            user = UserServices.create_user(email, password)
            return user
        except IntegrityError as e:
            raise HTTPException(status_code=400, detail=f"User with provided email - {email} already exists.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def create_super_user(email, password):
        """
        It creates a super user with the provided email and password
        @param email - The email address of the user.
        @param password - The password for the user.
        @returns The user object is being returned.
        """
        try:
            user = UserServices.create_super_user(email, password)
            return user
        except IntegrityError:
            raise HTTPException(status_code=400, detail=f"User with provided email - {email} already exists.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def login_user(email, password):
        """
        It takes an email and a password as parameters, and returns a JWT token if the user exists and the password is
        correct
        @param email - The email of the user
        @param password - The password to be hashed.
        @returns A JWT token
        """
        try:

            user = UserServices.login_user(email, password)
            user_id = UserServices.read_user_id_by_email(email)
            user = UserServices.update_user_is_active(user_id, is_active=True)
            if user.is_superuser:
                return signSuperUserJWT(user_id)
            return signClassicUserJWT(user.id)
        except UserInvalidePassword as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def logout_user(email):
        """
        It takes an email address as an argument, and returns a boolean value indicating whether the user was successfully
        logged out
        @param email - The email of the user to log out.
        @returns The user_id is being returned.
        """
        try:
            user_id = UserServices.read_user_id_by_email(email)
            return UserServices.update_user_is_active(user_id, is_active=False)

        except UserInvalidePassword as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_user_by_id(user_id: str):
        """
        > This function takes in a user_id and returns the user object if it exists, otherwise it raises an exception
        @param {str} user_id - str - this is the parameter that will be passed in the URL.
        @returns A user object
        """
        user = UserServices.get_user_by_id(user_id)
        if user:
            return user
        raise HTTPException(status_code=400, detail=f"user with provided id {user_id} does not exist")

    @staticmethod
    def get_all_users():
        """
        It returns all users
        @returns A list of all users
        """
        users = UserServices.get_all_users()
        return users

    @staticmethod
    def delete_user_by_id(user_id: str):
        """
        It deletes a user by id
        @param {str} user_id - str - this is the parameter that will be passed to the function.
        @returns Response object
        """
        try:
            UserServices.delete_user_by_id(user_id)
            return Response(content=f"User with id - {user_id} is deleted")
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e)) from e

    @staticmethod
    def update_user_is_active(user_id: str, is_active: bool):
        """
        It updates the user's is_active status.
        @param {str} user_id - str
        @param {bool} is_active - bool
        """
        try:
            UserServices.update_user_is_active(user_id, is_active)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def reserve_flight_by_flight_id_and_class_number(flight_id, class_number, user_id):
        """
        It reads the number of available tickets for a given flight, and if there are no available tickets, it raises an
        exception. If there are available tickets, it reads all the tickets for that flight, and returns the first ticket
        that is not reserved
        @param flight_id - The flight id of the flight you want to reserve a ticket for.
        @param class_number - 1, 2, 3, 4
        @returns A ticket object
        """
        try:
            number_of_available_tickets = TicketService.read_number_of_available_tickets_by_flight_id(flight_id)
            print(number_of_available_tickets)
            if number_of_available_tickets == 0:
                raise HTTPException(status_code=400, detail="There is no available ticket for this flight")
            else:
                tickets = TicketService.read_tickets_by_flight_id(flight_id)
                list_ticket = []
                for ticket in tickets:
                    if ticket.is_it_reserved == False:
                        list_ticket.append(ticket)

                ticket = list_ticket[0]
                ticket_id = ticket.ticket_id
                TicketService.update_is_it_reserved(ticket_id)
                ReservationService.create_new_reservation(ticket_id, user_id)
                return ticket
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e
