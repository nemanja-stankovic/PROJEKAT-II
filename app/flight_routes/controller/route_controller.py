from app.flight_routes.servicies import RouteService
from app.flight_routes.exceptions import RouteExceptionCode, RouteNotFoundException
from app.airports.services import AirportService
from fastapi import HTTPException, Response
from app.airports.exceptions import AirportNotFoundException

class RouteController:

    @staticmethod
    def create_new_route(from_airport_id, to_airport_id):
        """
        It creates a new route between two airports, if the airports exist and the route doesn't already exist
        @param from_airport_id - The ID of the airport from which the route starts.
        @param to_airport_id - The ID of the airport that the route is going to.
        @returns A route object
        """
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
        """
        It returns a list of all the routes in the database
        @returns A list of all the routes in the database.
        """
        routes = RouteService.read_all_routes()
        return routes

    @staticmethod
    def get_all_route_ids_by_city(city):
        """
        This function returns a list of all route ids for a given city
        @param city - The city that the route is in.
        @returns A list of route ids
        """
        route_ids = RouteService.read_all_route_ids_by_city(city)
        return route_ids

    @staticmethod
    def get_route_by_id(route_id: str):
        """
        > This function returns a route by id
        @param {str} route_id - The route ID to be searched for.
        @returns A route object
        """
        try:
            route = RouteService.read_route_by_id(route_id)
            return route
        except RouteNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_route_by_id(route_id: str):
        """
        It deletes a route by its ID.
        @param {str} route_id - str - the ID of the route to be deleted
        @returns A response object with the content and status code.
        """
        try:
            RouteService.delete_route_by_id(route_id)
            return Response(content=f"Airport with provided ID: {route_id} deleted.", status_code=200)
        except RouteNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
