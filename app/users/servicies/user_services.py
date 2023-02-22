
import hashlib

from app.users.repositories.user_repository import UserRepository

from app.db.database import SessionLocal
from app.users.exceptions import UserInvalidePassword


class UserServices:

    @staticmethod
    def create_user(email, password: str):
        """
        It creates a user with the given email and password
        @param email - str
        @param {str} password - str
        @returns The user object
        """
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                hashed_password = hashlib.sha256(bytes(password,"utf-8")).hexdigest()
                return user_repository.create_user(email, hashed_password)
            except Exception as e:
                raise e

    @staticmethod
    def create_super_user(email, password):
        """
        It creates a super user with the given email and password
        @param email - The email address of the user
        @param password - The password you want to hash
        @returns The user object
        """
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                hashed_password = hashlib.sha256(bytes(password,"utf-8")).hexdigest()
                return user_repository.create_super_user(email, hashed_password)
            except Exception as e:
                raise e

    @staticmethod
    def get_user_by_id(user_id: str):
        """
        > This function gets a user by id
        @param {str} user_id - The user's ID.
        @returns A user object
        """
        with SessionLocal() as db:
            user_repository = UserRepository(db)
            return user_repository.get_user_by_id(user_id)

    @staticmethod
    def get_all_users():
        """
        It gets all users from the database
        @returns A list of all users in the database.
        """
        with SessionLocal() as db:
            user_repository = UserRepository(db)
            return user_repository.get_all_users()

    @staticmethod
    def delete_user_by_id(user_id: str):
        """
        It deletes a user from the database by their id
        @param {str} user_id - str
        @returns The user_repository.delete_user_by_id(user_id) is returning the user_id of the user that was deleted.
        """
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.delete_user_by_id(user_id)
        except Exception as e:
            raise e

    @staticmethod
    def update_user_is_active(user_id: str, is_active: bool):
        """
        It updates the user's is_active status in the database
        @param {str} user_id - str
        @param {bool} is_active - bool
        @returns The user_repository.update_user_is_active(user_id, is_active) is being returned.
        """
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                return user_repository.update_user_is_active(user_id, is_active)
            except Exception as e:
                raise e

    @staticmethod
    def login_user(email: str, password: str):
        """
        It takes an email and password, and returns a user if the password is correct
        @param {str} email - str, password: str
        @param {str} password - The password to be hashed.
        @returns The user object
        """
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                user = user_repository.read_user_by_email(email)
                if hashlib.sha256(bytes(password, "utf-8")).hexdigest() != user.password:
                    raise UserInvalidePassword(message="Invalid password for user", code=401)
                return user
            except Exception as e:
                raise e

    @staticmethod
    def read_user_by_email(user_email: str):
        """
        It takes a user's email address as a string, and returns the user's ID as an integer
        @param {str} user_email - str
        @returns The user_id of the user with the given email.
        """
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.read_user_id_by_email(user_email)
        except Exception as e:
            raise e

    @staticmethod
    def read_user_id_by_email(user_email: str):
        """
        It reads a user's id from the database by their email
        @param {str} user_email - str
        @returns The user_id is being returned.
        """
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                user_id = user_repository.read_user_id_by_email(user_email)
                return user_id
        except Exception as e:
            raise e