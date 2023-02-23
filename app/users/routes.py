"""
`reserve_flight_by_flight_id_and_class_number` takes a flight id and a class number and returns a ticket object.
@param {UserSchemaIn} user - UserSchemaIn
@returns A ticket object
"""
from fastapi import APIRouter, Depends
from app.users.controller import UserController
from app.users.schemas import UserSchema, UserSchemaIn
from app.users.controller.user_auth_controller import JWTClassicUserBearer,JWTSuperUserBearer
from app.tickets.schemas import TicketSchema

user_router = APIRouter(tags=["Users"], prefix="/api/users")


@user_router.post("/add-new-user", response_model=UserSchema)
def create_user(user: UserSchemaIn):
    """
    `create_user` takes a `UserSchemaIn` object and returns a `User` object
    @param {UserSchemaIn} user - UserSchemaIn
    @returns A user object
    """
    return UserController.create_user(user.email, user.password)

@user_router.post("/add-new-super-user", response_model=UserSchema, dependencies=[Depends(JWTSuperUserBearer())])
def create_super_user(user: UserSchemaIn):
    """
    `create_super_user` creates a super user
    @param {UserSchemaIn} user - UserSchemaIn
    @returns A user object
    """
    return UserController.create_super_user(user.email, user.password)

@user_router.post("/login")
def user_login(user: UserSchemaIn):
    """
    `user_login` takes a `UserSchemaIn` object and returns a `UserSchemaOut` object
    @param {UserSchemaIn} user - UserSchemaIn
    @returns A user object
    """
    return UserController.login_user(user.email, user.password)

@user_router.post("/logout", dependencies=[Depends(JWTClassicUserBearer())])
def user_logout(email: str):
    """
    `Logs out a user.`
    @param {str} email - str
    @returns A dictionary with the key 'message' and the value 'Successfully logged out'
    """
    return UserController.logout_user(email)

@user_router.get("/id", response_model=UserSchema, dependencies=[Depends(JWTSuperUserBearer())])
def get_user_by_id(user_id: str):
    """
    `get_user_by_id` returns a user object given a user id
    @param {str} user_id - The user's ID.
    @returns A user object
    """
    return UserController.get_user_by_id(user_id)

@user_router.get("/get-all-users", response_model=list[UserSchema])
def get_all_users():
    """
    `get_all_users()` returns a list of all users
    @returns A list of all users in the database.
    """
    return UserController.get_all_users()

@user_router.delete("/", dependencies=[Depends(JWTSuperUserBearer())])
def delete_user_by_id(user_id: str):
    """
    `delete_user_by_id` deletes a user by id
    @param {str} user_id - str
    @returns The return value is the result of the delete_user_by_id function.
    """
    return UserController.delete_user_by_id(user_id)

@user_router.put("/update/is_active", response_model=UserSchema, dependencies=[Depends(JWTClassicUserBearer())])
def update_user_is_active(user_id: str, is_active: bool):
    """
    `update_user` updates a user's is_active status
    @param {str} user_id - str
    @param {bool} is_active - bool
    @returns The return value is the result of the update_user_is_active function.
    """
    return UserController.update_user_is_active(user_id, is_active)

@user_router.get("/reserve-flight", response_model=TicketSchema, dependencies=[Depends(JWTClassicUserBearer())])
def reserve_flight_by_flight_id_and_class_number(flight_id, class_number, user_id):
    """
    Reserve a flight by flight id and class number
    @param flight_id - the id of the flight you want to reserve
    @param class_number - 1 for first class, 2 for business class, 3 for economy class
    @returns A list of all the flights that are available for the given date.
    """
    return UserController.reserve_flight_by_flight_id_and_class_number(flight_id,class_number, user_id)

@user_router.put("/update/password", response_model=UserSchema, dependencies=[Depends(JWTClassicUserBearer())])
def update_user_password(email: str, old_password: str, new_password: str):
    """
    `update_user_password` updates the password of a user

    :param email: str
    :type email: str
    :param password: str
    :type password: str
    :return: A boolean value
    """

    return UserController.update_user_password(email, old_password, new_password)
