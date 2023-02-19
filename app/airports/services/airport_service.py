from sqlalchemy.exc import IntegrityError

from app.airports.models import Airport
from app.db import SessionLocal
from app.airports.repositories import AirportRepository
from app.airports.exceptions import AirportExceptionCode


class AirportService:

    @staticmethod
    def create_new_airport(airport_name, city, country):
        try:
            with SessionLocal() as db:
                repository = AirportRepository(db)
                airport = repository.read_airport_by_name(airport_name)
                if bool(airport) is False:
                    return repository.create_airport(airport_name, city, country)
                raise AirportExceptionCode(message="Airport name already exists in database.", code=400)
        except Exception as e:
            raise e



    @staticmethod
    def read_all_airports():
        try:
            with SessionLocal() as db:
                repository = AirportRepository(db)
                return repository.read_all_airports()
        except Exception as e:
            raise e

    @staticmethod
    def read_airport_by_id(airport_id):
        try:
            with SessionLocal() as db:
                repository = AirportRepository(db)
                return repository.read_airport_by_id(airport_id)
        except Exception as e:
            raise e

    @staticmethod
    def delete_airport_by_id(airport_id):
        try:
            with SessionLocal() as db:
                repository = AirportRepository(db)
                return repository.delete_airport(airport_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_airport_by_name(airport_name):
        try:
            with SessionLocal() as db:
                repository = AirportRepository(db)
                return repository.read_airport_by_name(airport_name)
        except Exception as e:
            raise e

    @staticmethod
    def read_all_airports_in_city(city):
        try:
            with SessionLocal() as db:
                repository = AirportRepository(db)
                return repository.read_airports_by_city(city)
        except Exception as e:
            raise e

    @staticmethod
    def read_all_airport_id_by_city(city):
        try:
            with SessionLocal() as db:
                repository = AirportRepository(db)
                return repository.read_airports_ids_by_city(city)
        except Exception as e:
            raise e