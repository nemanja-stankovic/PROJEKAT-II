from fastapi import APIRouter
from app.flight_routes.controller import RouteController
from app.flight_routes.schemas import RouteSchema, RouteSchemaIn


flight_route_router = APIRouter(tags=["Flight routes"], prefix="/api/flight-routes")


@flight_route_router.post("/create-new-route", response_model=RouteSchema)
def create_new_route(route: RouteSchemaIn):
    return RouteController.create_new_route(from_airport_id=route.from_airport_id, to_airport_id=route.to_airport_id)


@flight_route_router.get("/get-all-routes", response_model=list[RouteSchema])
def get_all_routes():
    routes = RouteController.get_all_routes()
    return routes

@flight_route_router.get("/get-all-route-ids-by-city", response_model=list)
def get_all_route_ids_by_city(city):
    route_ids = RouteController.get_all_route_ids_by_city(city)
    return route_ids



@flight_route_router.get("/get-route-by-id", response_model=RouteSchema)
def get_route_by_id(route_id: str):
    return RouteController.get_route_by_id(route_id)


@flight_route_router.delete("/delete-route")
def delete_route_by_id(route_id: str):
    return RouteController.delete_route_by_id(route_id)