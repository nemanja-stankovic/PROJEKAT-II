from app.flight_routes.servicies import RouteService
from app.flight_routes.exceptions import RouteExceptionCode, RouteNotFoundException
from app.airports.services import AirportService
from fastapi import HTTPException, Response
from app.airports.exceptions import AirportNotFoundException

class RouteController:

    @staticmethod
    def create_new_route(from_airport_id, to_airport_id):
        try:
            AirportService.read_airport_by_id(from_airport_id)
            AirportService.read_airport_by_id(to_airport_id)
            if from_airport_id != to_airport_id:
                route = RouteService.create_new_route(from_airport_id, to_airport_id)
                return route
            else:
                raise RouteExceptionCode(message="from_airport_id and to_airport_id must be different", code=400)
        except AirportNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except RouteExceptionCode as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_routes():
        routes = RouteService.read_all_routes()
        return routes

    @staticmethod
    def get_all_route_ids_by_city(city):
        route_ids = RouteService.read_all_route_ids_by_city(city)
        return route_ids

    @staticmethod
    def get_route_by_id(route_id: str):
        try:
            route = RouteService.read_route_by_id(route_id)
            return route
        except RouteNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_route_by_id(route_id: str):
        try:
            RouteService.delete_route_by_id(route_id)
            return Response(content=f"Airport with provided ID: {route_id} deleted.", status_code=200)
        except RouteNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
