from pandas.core.computation.expr import intersection

from app.flight_routes.models import Route
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.flight_routes.exceptions import RouteNotFoundException
from app.airports.models import Airport

class RouteRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_route(self, from_airport_id, to_airport_id):
        """
        It creates a new route in the database
        @param from_airport_id - The ID of the airport that the route is departing from.
        @param to_airport_id - The airport id of the destination airport
        @returns The route object is being returned.
        """
        try:
            route = Route(from_airport_id=from_airport_id,to_airport_id=to_airport_id)
            self.db.add(route)
            self.db.commit()
            self.db.refresh(route)
            return route
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    def read_all_routes(self):
        """
        It returns all the routes in the database
        @returns A list of all the routes in the database.
        """
        routes = self.db.query(Route).all()
        return routes

    def read_route_by_id(self, route_id: str):
        """
        It takes a route_id as a string, and returns a route object
        @param {str} route_id - str - the route ID to search for
        @returns The route object is being returned.
        """
        route = self.db.query(Route).filter(Route.route_id == route_id).first()
        if route is None:
            raise RouteNotFoundException(f"Route with provided ID: {route_id} not found.", 400)
        return route

    def delete_route(self, route_id: str):
        """
        It deletes a route from the database
        @param {str} route_id - The ID of the route to be deleted.
        @returns True
        """
        try:
            route = self.db.query(Route).filter(Route.route_id == route_id).first()
            if route is None:
                raise RouteNotFoundException(f"Route with provided ID: {route_id} not found.", 400)
            self.db.delete(route)
            self.db.commit()
            # self.db.refresh(airport)
            return True
        except Exception as e:
            raise e

    def read_routes_by_from_airport_id(self, from_airport_id: str):
        """
        It returns all routes that have a from_airport_id that matches the provided from_airport_id
        @param {str} from_airport_id - str
        @returns A list of routes
        """
        routes = self.db.query(Route).filter(Route.from_airport_id == from_airport_id).all()
        if bool(routes) is False:
            raise RouteNotFoundException(f"Route with provided ID: {from_airport_id} not found.", 400)
        return routes

    def read_routes_ids_by_from_airport_id(self, from_airport_id: str):
        """
        It returns a list of route_ids for a given from_airport_id
        @param {str} from_airport_id - str
        @returns A list of route_ids
        """
        routes = self.db.query(Route).filter(Route.from_airport_id == from_airport_id).all()
        if bool(routes) is False:
            raise RouteNotFoundException(f"Route with provided ID: {from_airport_id} not found.", 400)
        route_ids_lst = []
        for route in routes:
            route_ids_lst.append(route.route_id)
        return route_ids_lst

    def read_routes_ids_by_to_airport_id(self, to_airport_id: str):
        """
        It returns a list of route_ids that have the same to_airport_id as the one provided
        @param {str} to_airport_id - str
        @returns A list of route_ids
        """
        routes = self.db.query(Route).filter(Route.to_airport_id == to_airport_id).all()
        if bool(routes) is False:
            raise RouteNotFoundException(f"Route with provided ID: {to_airport_id} not found.", 400)
        route_ids_lst = []
        for route in routes:
            route_ids_lst.append(route.route_id)
        return route_ids_lst

    def read_route_by_from_airport_id(self,from_airport_id: str):
        """
        This function takes in a from_airport_id and returns a list of routes that have that from_airport_id
        @param {str} from_airport_id - str
        @returns A list of routes with the same from_airport_id
        """
        route = self.db.query(Route).filter(Route.from_airport_id == from_airport_id).all()
        if bool(route) is not False:
            return route
        else:
            raise RouteNotFoundException(f"Route id with provided from_airport_id: {from_airport_id} not found.", 400)

    def read_route_by_to_airport_id(self,to_airport_id: str):
        """
        It returns a list of all routes that have a to_airport_id that matches the to_airport_id provided as an argument
        @param {str} to_airport_id - str
        @returns A list of routes with the provided to_airport_id
        """
        route = self.db.query(Route).filter(Route.to_airport_id == to_airport_id).all()
        if bool(route) is not False:
            return route
        else:
            raise RouteNotFoundException(f"Route id with provided to_airport_id: {to_airport_id} not found.", 400)

