from sqlalchemy.exc import IntegrityError

from app.airports.models import Airport
from app.db import SessionLocal
from app.flight_routes.repositories import RouteRepository
from app.flight_routes.exceptions import RouteExceptionCode
from app.airports.services import AirportService

class RouteService:

    @staticmethod
    def create_new_route(from_airport_id, to_airport_id):
        """
        It creates a new route in the database
        @param from_airport_id - The ID of the airport that the route is departing from.
        @param to_airport_id - The ID of the airport you want to fly to.
        @returns The route object
        """
        try:
            with SessionLocal() as db:
                repository = RouteRepository(db)
                return repository.create_route(from_airport_id, to_airport_id)
        except Exception as e:
            raise e


    @staticmethod
    def read_all_routes():
        """
        It reads all routes from the database
        @returns A list of all the routes in the database.
        """
        try:
            with SessionLocal() as db:
                repository = RouteRepository(db)
                return repository.read_all_routes()
        except Exception as e:
            raise e

    @staticmethod
    def read_route_by_id(route_id):
        """
        It reads a route by id
        @param route_id - The id of the route you want to read.
        @returns A route object
        """
        try:
            with SessionLocal() as db:
                repository = RouteRepository(db)
                return repository.read_route_by_id(route_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_route_by_from_id(from_airport_id):
        """
        It takes an airport id as an argument and returns a list of routes that have that airport id as their
        from_airport_id
        @param from_airport_id - The ID of the airport you want to find routes from.
        @returns A list of routes
        """
        try:
            with SessionLocal() as db:
                repository = RouteRepository(db)
                return repository.read_route_by_from_airport_id(from_airport_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_route_by_to_id(to_airport_id):
        """
        It takes an airport id as an argument, and returns a list of routes that have that airport id as their destination
        @param to_airport_id - The id of the airport you want to fly to.
        @returns A list of routes that have the to_airport_id
        """
        try:
            with SessionLocal() as db:
                repository = RouteRepository(db)
                return repository.read_route_by_to_airport_id(to_airport_id)
        except Exception as e:
            raise e

    @staticmethod
    def read_all_route_ids_by_cities(from_city, to_city):
        """
        It takes two cities as input and returns a list of route ids that have a route from the first city to the second
        city
        @param from_city - The city where the flight is departing from.
        @param to_city - The city you want to fly to.
        @returns list of route_ids
        """
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
        """
        It deletes a route from the database by its id
        @param route_id - The id of the route to be deleted.
        @returns The route_id of the route that was deleted.
        """
        try:
            with SessionLocal() as db:
                repository = RouteRepository(db)
                return repository.delete_route(route_id)
        except Exception as e:
            raise e
