from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.users.models import User


class UserRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_user(self, email, password):
        """
        It creates a new user and adds it to the database
        @param email - The email address of the user.
        @param password - The password to be hashed.
        @returns The user object is being returned.
        """
        try:
            user = User(email, password)
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except IntegrityError as e:
            raise e

    def create_super_user(self, email, password):
        """
        It creates a super user with the given email and password
        @param email - The email address of the user.
        @param password - The password to be hashed and stored.
        @returns The user object is being returned.
        """
        try:
            user = User(email=email, password=password, is_superuser=True)
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except IntegrityError as e:
            raise e

    def get_user_by_id(self, user_id: str):
        """
        It returns a user object from the database, given a user id
        @param {str} user_id - The user's ID.
        @returns The user object
        """
        user = self.db.query(User).filter(User.id == user_id).first()
        return user

    def get_all_users(self):
        """
        It returns all the users in the database
        @returns A list of all the users in the database.
        """
        users = self.db.query(User).all()
        return users

    def delete_user_by_id(self, user_id:str):
        """
        It deletes a user from the database by their id
        @param {str} user_id - The id of the user to be deleted.
        @returns True or False
        """
        try:
            user = self.db.query(User).filter(User.id == user_id).first()
            self.db.delete(user)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_user_is_active(self, user_id: str, is_active: bool):
        """
        It updates the user's is_active status in the database
        @param {str} user_id - str
        @param {bool} is_active - bool
        @returns The user object
        """
        try:
            user = self.db.query(User).filter(User.id == user_id).first()
            user.is_active = is_active
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except Exception as e:
            raise e

    def update_user_password(self, email: str, password: str):
        """
        It updates the user's password in the database

        :param email: str
        :type email: str
        :return: The user object is being returned.
        """
        try:
            user = self.db.query(User).filter(User.email == email).first()
            user.password = password
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except Exception as e:
            raise e

    def read_user_by_email(self, email: str):
        """
        It returns the first user in the database whose email matches the email passed in as an argument
        @param {str} email - str
        @returns The user object
        """
        try:
            user = self.db.query(User).filter(User.email == email).first()
            if user:
                return user
        except Exception as e:
            raise e

    def read_user_id_by_email(self, email: str):
        """
        > This function takes an email address as an argument and returns the user ID associated with that email address
        @param {str} email - str
        @returns The user id.
        """
        try:
            user = self.db.query(User).filter(User.email == email).first()
            if user:
                return user.id
        except Exception as e:
            raise e

