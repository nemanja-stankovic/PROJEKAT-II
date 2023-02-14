from fastapi import APIRouter, Depends
from app.users.controller import UserController
from app.users.schemas import *
from app.users.controller.user_auth_controller import JWTClassicUserBearer,JWTSuperUserBearer



user_router = APIRouter(tags=["users"], prefix="/api/users")


@user_router.post("/add-new-user", response_model=UserSchema)
def create_user(user: UserSchemaIn):
    return UserController.create_user(user.email, user.password)


@user_router.post("/add-new-super-user", response_model=UserSchema, dependencies=[Depends(JWTSuperUserBearer())])
def create_super_user(user: UserSchemaIn):
    return UserController.create_super_user(user.email, user.password)

@user_router.post("/login")
def user_login(user: UserSchemaIn):
    return UserController.login_user(user.email, user.password)

@user_router.get("/id", response_model=UserSchema, dependencies=[Depends(JWTSuperUserBearer())])
def get_user_by_id(user_id: str):
    return UserController.get_user_by_id(user_id)


@user_router.get("/get-all-users", response_model=list[UserSchema])
def get_all_users():
    return UserController.get_all_users()


@user_router.delete("/", dependencies=[Depends(JWTSuperUserBearer())])
def delete_user_by_id(user_id: str):
    return UserController.delete_user_by_id(user_id)


@user_router.put("/update/is_active", response_model=UserSchema)
def update_user(user_id: str, is_active: bool):
    return UserController.update_user_is_active(user_id, is_active)

