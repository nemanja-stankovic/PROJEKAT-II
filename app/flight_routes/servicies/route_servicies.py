from sqlalchemy.exc import IntegrityError

from app.airports.models import Airport
from app.db import SessionLocal
from app.flight_routes.repositories import RouteRepository
from app.flight_routes.exceptions import RouteExceptionCode
from app.airports.services import AirportService

class RouteService:

    @staticmethod
    def create_new_route(from_airport_id, to_airport_id):
        try:
            with SessionLocal() as db:
                repository = RouteRepository(db)
                return repository.create_route(from_airport_id, to_airport_id)
        except Exception as e:
            raise e


    @staticmethod
    def read_all_routes():
        try:
            with SessionLocal() as db:
                repository = RouteRepository(db)
                return repository.read_all_routes()
        except Exception as e:
            raise e

    @staticmethod
    def read_route_by_id(route_id):
        try:
            with SessionLocal() as db:
                repository = RouteRepository(db)
                return repository.read_route_by_id(route_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_route_by_from_id(from_airport_id):
        try:
            with SessionLocal() as db:
                repository = RouteRepository(db)
                return repository.read_route_by_from_airport_id(from_airport_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_route_by_to_id(to_airport_id):
        try:
            with SessionLocal() as db:
                repository = RouteRepository(db)
                return repository.read_route_by_to_airport_id(to_airport_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_all_route_ids_by_cities(from_city, to_city):
        try:
            with SessionLocal() as db:
                repository = RouteRepository(db)
                airport_ids_lst_from = AirportService.read_all_airport_id_by_city(from_city)

                list_route_ids_from = []
                for airport_id in airport_ids_lst_from:
                    route_ids_from = repository.read_routes_ids_by_from_airport_id(airport_id)
                    for route_id in route_ids_from:
                        list_route_ids_from.append(route_id)

                airport_ids_lst_to = AirportService.read_all_airport_id_by_city(to_city)

                list_route_ids_to = []
                for airport_id in airport_ids_lst_to:
                    route_ids_to = repository.read_routes_ids_by_to_airport_id(airport_id)
                    for route_id in route_ids_to:
                        list_route_ids_to.append(route_id)
                result = []
                for route_id_from in list_route_ids_from:
                    for route_id_to in list_route_ids_to:
                        if route_id_to == route_id_from:
                            result.append(route_id_to)
                set_result = set(result)
                result = list(set_result)
                return result
        except Exception as e:
            raise e


    @staticmethod
    def delete_route_by_id(route_id):
        try:
            with SessionLocal() as db:
                repository = RouteRepository(db)
                return repository.delete_route(route_id)
        except Exception as e:
            raise e
