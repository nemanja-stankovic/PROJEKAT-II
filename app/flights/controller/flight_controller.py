
from app.flights.exceptions import FlightExceptionCode, FlightNotFoundException
from app.flights.servicies import FlightService
from fastapi import HTTPException, Response
from app.flight_routes.servicies import RouteService
from app.airports.services import AirportService

def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

class FlightController:

    @staticmethod
    def create_new_flight(departure_time, arrival_time, airline, num_of_seats, route_id):
        try:
            flight = FlightService.create_new_flight(departure_time, arrival_time, airline, num_of_seats, route_id)
            return flight
        except FlightExceptionCode as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            print(str(e))
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_flights():
        flights = FlightService.read_all_flights()
        return flights

    @staticmethod
    def search_flights_by_route_id(route_id):
        flights = FlightService.read_all_flights()
        flights_list=[]
        for flight in flights:
            if route_id == flight.route_id:
                flights_list.append(flight)
        return flights_list


    @staticmethod
    def search_flights_by_from_city(from_city):
        try:
            from_airport_id_lst = AirportService.read_all_airport_id_by_city(from_city)
            route_ids = []
            for from_id in from_airport_id_lst:
                route_lst = RouteService.read_route_by_from_id(from_id)
                for route in route_lst:
                    route_id = route.route_id
                    route_ids.append(route_id)
            flight_list = []
            for route_id in route_ids:
                flights = FlightService.read_flights_by_route_id(route_id)
                for flight in flights:
                    flight_list.append(flight)
            return flight_list[:6]
        except FlightNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def search_flights_by_to_city(to_city):
        try:
            to_airport_id_lst = AirportService.read_all_airport_id_by_city(to_city)
            route_ids = []
            for to_id in to_airport_id_lst:
                route_lst = RouteService.read_route_by_to_id(to_id)
                for route in route_lst:
                    route_id = route.route_id
                    route_ids.append(route_id)
            flight_list = []
            for route_id in route_ids:
                flights = FlightService.read_flights_by_route_id(route_id)
                for flight in flights:
                    flight_list.append(flight)
            return flight_list[:6]
        except FlightNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_flight_by_id(flight_id: str):
        try:
            flight = FlightService.read_flight_by_id(flight_id)
            return flight
        except FlightNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))


    @staticmethod
    def delete_flight_by_id(flight_id: str):
        try:
            FlightService.delete_flight_by_id(flight_id)
            return Response(content=f"Flight with provided ID: {flight_id} deleted.", status_code=200)
        except FlightNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def search_flights_by_cities(from_city: str, to_city: str):
            flights_from = FlightController.search_flights_by_from_city(from_city)
            flights_to = FlightController.search_flights_by_to_city(to_city)
            flights = []
            for flight_from in flights_from:
                for flight_to in flights_to:
                    if flight_from.route_id == flight_to.route_id:
                        flights.append(flight_from)
            list_searched_flights=[]
            for flight in flights:
                searched_flight=flight
                setattr(searched_flight,"from_city",from_city)
                setattr(searched_flight, "to_city", to_city)
                list_searched_flights.append(searched_flight)

            if len(list_searched_flights) >0:
                return list_searched_flights
            else:
                raise HTTPException(status_code=400, detail=f"There is no flight from city {from_city} and to_city {to_city}")

    @staticmethod
    def search_flights_by_departure_date(departure_date):
        try:
            flight = FlightService.read_flights_by_departure_date(departure_date)
            return flight
        except FlightNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
