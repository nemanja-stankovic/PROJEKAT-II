from pandas.core.computation.expr import intersection

from app.flight_routes.models import Route
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.flight_routes.exceptions import RouteNotFoundException

class RouteRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_route(self, from_airport_id, to_airport_id):
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
        routes = self.db.query(Route).all()
        return routes

    def read_route_by_id(self, route_id: str):
        route = self.db.query(Route).filter(Route.route_id == route_id).first()
        if route is None:
            raise RouteNotFoundException(f"Route with provided ID: {route_id} not found.", 400)
        return route

    def delete_route(self, route_id: str):
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
        routes = self.db.query(Route).filter(Route.from_airport_id == from_airport_id).all()
        if bool(routes) is False:
            raise RouteNotFoundException(f"Route with provided ID: {from_airport_id} not found.", 400)
        return routes

    def read_routes_ids_by_from_airport_id(self, from_airport_id: str):
        routes = self.db.query(Route).filter(Route.from_airport_id == from_airport_id).all()
        print(routes)
        if bool(routes) is False:
            raise RouteNotFoundException(f"Route with provided ID: {from_airport_id} not found.", 400)
        route_ids_lst = []
        for route in routes:
            route_ids_lst.append(route.route_id)
        print(route_ids_lst)
        return route_ids_lst

    def read_routes_ids_by_to_airport_id(self, to_airport_id: str):
        routes = self.db.query(Route).filter(Route.to_airport_id == to_airport_id).all()
        print(routes)
        if bool(routes) is False:
            raise RouteNotFoundException(f"Route with provided ID: {to_airport_id} not found.", 400)
        route_ids_lst = []
        for route in routes:
            route_ids_lst.append(route.route_id)
        print(route_ids_lst)
        return route_ids_lst

    def read_route_by_from_airport_id(self,from_airport_id: str):
        route = self.db.query(Route).filter(Route.from_airport_id == from_airport_id).all()
        if bool(route) is not False:
            return route
        else:
            raise RouteNotFoundException(f"Route id with provided from_airport_id: {from_airport_id} not found.", 400)

    def read_route_by_to_airport_id(self,to_airport_id: str):
        route = self.db.query(Route).filter(Route.to_airport_id == to_airport_id).all()
        if bool(route) is not False:
            return route
        else:
            raise RouteNotFoundException(f"Route id with provided to_airport_id: {to_airport_id} not found.", 400)


    # def read_route_by_name(self, airport_name):
    #     airport = self.db.query(Airport).filter(Airport.airport_name == airport_name).first()
    #     return airport