from fastapi import APIRouter, Depends
from app.flight_routes.controller import RouteController
from app.flight_routes.schemas import RouteSchema, RouteSchemaIn
from app.users.controller.user_auth_controller import JWTSuperUserBearer

flight_route_router = APIRouter(tags=["Flight routes"], prefix="/api/flight-routes")


@flight_route_router.post("/create-new-route", response_model=RouteSchema, dependencies=[Depends(JWTSuperUserBearer())])
def create_new_route(route: RouteSchemaIn):
    """
    "Create a new route from the given airport to the given airport."

    The function is defined in the `RouteController` class, which is a class that contains all the functions that are
    related to routes
    @param {RouteSchemaIn} route - RouteSchemaIn
    @returns A route object
    """
    return RouteController.create_new_route(from_airport_id=route.from_airport_id, to_airport_id=route.to_airport_id)


@flight_route_router.get("/get-all-routes", response_model=list[RouteSchema])
def get_all_routes():
    """
    It returns all the routes in the database.
    @returns A list of all the routes in the database.
    """
    routes = RouteController.get_all_routes()
    return routes

@flight_route_router.get("/get-all-route-ids-by-city", response_model=list)
def get_all_route_ids_by_city(city):
    """
    This function returns a list of all route ids for a given city
    @param city - The city you want to get the route ids for.
    @returns A list of route ids
    """
    route_ids = RouteController.get_all_route_ids_by_city(city)
    return route_ids



@flight_route_router.get("/get-route-by-id", response_model=RouteSchema)
def get_route_by_id(route_id: str):
    """
    `get_route_by_id` returns a route object given a route id
    @param {str} route_id - The id of the route you want to get.
    @returns A route object
    """
    return RouteController.get_route_by_id(route_id)


@flight_route_router.delete("/delete-route", dependencies=[Depends(JWTSuperUserBearer())])
def delete_route_by_id(route_id: str):
    """
    Delete a route by id
    @param {str} route_id - The id of the route to delete
    @returns The route_id of the route that was deleted.
    """
    return RouteController.delete_route_by_id(route_id)