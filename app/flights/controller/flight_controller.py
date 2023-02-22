
from app.flights.exceptions import FlightExceptionCode, FlightNotFoundException
from app.flights.servicies import FlightService
from fastapi import HTTPException, Response
from app.flight_routes.servicies import RouteService
from app.tickets.servicies import TicketService
from app.airports.services import AirportService
from app.tickets.controller import TicketController
from app.flight_routes.exceptions import RouteNotFoundException
from app.flights.servicies import ViewFlightService
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
            flights = FlightService.read_flights_by_departure_date(departure_date)
            return flights
        except FlightNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def search_available_flights_by_departure_date(departure_date):
        try:
            flights = FlightService.read_available_flights_by_departure_date(departure_date)
            return flights
        except FlightNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def search_flights_by_cities_and_dates(from_city: str, to_city: str, departure_date: str, arrival_date: str):
        try:
            route_ids = RouteService.read_all_route_ids_by_cities(from_city, to_city)
        except RouteNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=f"There is no route from {from_city} to {to_city} ")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        try:
            flight_ids_by_route = []
            for route_id in route_ids:
                flights_by_route = FlightService.read_flights_by_route_id(route_id)

                for flight in flights_by_route:
                    flight_id_by_route = flight.flight_id
                    flight_ids_by_route.append(flight_id_by_route)
            flights_by_dep_date = FlightService.read_flights_by_departure_date(departure_date)
            flights_by_arr_date = FlightService.read_flights_by_arrival_date(arrival_date)

            flight_ids_by_dep_date = []
            for flight in flights_by_dep_date:
                flight_id_by_dep_date = flight.flight_id
                flight_ids_by_dep_date.append(flight_id_by_dep_date)

            flight_ids_by_arr_date = []
            for flight in flights_by_arr_date:
                flight_id_by_arr_date = flight.flight_id
                flight_ids_by_arr_date.append(flight_id_by_arr_date)

            result = []

            for flight_id_r in flight_ids_by_route:
                for flight_id_d in flight_ids_by_dep_date:
                    if flight_id_r == flight_id_d:
                        result.append(flight_id_r)
            result_2 = []
            for flight_id_r in result:
                for flight_id_d in flight_ids_by_arr_date:
                    if flight_id_r == flight_id_d:
                        result_2.append(flight_id_r)
            set_result = set(result_2)
            result = list(set_result)
            list_results = []
            for flight_id in result:
                flight = FlightService.read_flight_by_id(flight_id)
                flight_id = flight_id
                departure_time = flight.departure_time
                arrival_time = flight.arrival_time
                airline = flight.airline
                num_of_seats = flight.num_of_seats
                num_of_available_tickets_first_class = TicketService.read_number_of_available_tickets_by_flight_id_and_class_number(flight_id,1)
                num_of_available_tickets_second_class = TicketService.read_number_of_available_tickets_by_flight_id_and_class_number(flight_id, 2)

                if num_of_available_tickets_first_class == 0 and num_of_available_tickets_second_class == 0:
                    continue
                price_first_class = TicketService.read_price_by_class_and_flight_id(1,flight_id)
                price_second_class = TicketService.read_price_by_class_and_flight_id(2,flight_id)
                from_city = from_city
                to_city = to_city

                view_flight = ViewFlightService.create_new_view_flight(flight_id, departure_time, arrival_time, airline,
                                                                       num_of_seats, num_of_available_tickets_first_class,
                                                                       num_of_available_tickets_second_class, price_first_class,
                                                                       price_second_class, from_city, to_city)
            view_flights = ViewFlightService.sort_view_flights_by_price()
            ViewFlightService.delete_view_flight()
            return view_flights[:3]
        except FlightNotFoundException as e:
            print(str(e))
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def explore_everywhere(departure_date: str, from_city: str):
        try:
            from_airport_id_lst = AirportService.read_all_airport_id_by_city(from_city)
            route_ids = []
            for from_id in from_airport_id_lst:
                route_lst = RouteService.read_route_by_from_id(from_id)
                for route in route_lst:
                    route_id = route.route_id
                    route_ids.append(route_id)
            flight_list_id_from = []
            for route_id in route_ids:
                flights_by_from = FlightService.read_flights_by_route_id(route_id)
                for flight in flights_by_from:
                    flight_list_id_from.append(flight.flight_id)
            flight_list_id_date = []
            flights_by_date = FlightService.read_available_flights_by_departure_date(departure_date)
            for flight in flights_by_date:
                flight_list_id_date.append(flight.flight_id)
            flight_list_ids = intersection(flight_list_id_date, flight_list_id_from)
            flight_list = []
            for flight_id in flight_list_ids:
                flight = FlightService.read_flight_by_id(flight_id)
                flight_id = flight_id
                departure_time = flight.departure_time
                arrival_time = flight.arrival_time
                airline = flight.airline
                num_of_seats = flight.num_of_seats
                num_of_available_tickets_first_class = TicketService.read_number_of_available_tickets_by_flight_id_and_class_number(
                    flight_id, 1)
                num_of_available_tickets_second_class = TicketService.read_number_of_available_tickets_by_flight_id_and_class_number(
                    flight_id, 2)
                if num_of_available_tickets_first_class == 0 and num_of_available_tickets_second_class == 0:
                    continue
                price_first_class = TicketService.read_price_by_class_and_flight_id(1,flight_id)
                price_second_class = TicketService.read_price_by_class_and_flight_id(2,flight_id)
                from_city = from_city
                route_id = flight.route_id
                route = RouteService.read_route_by_id(route_id)
                airport_id = route.to_airport_id
                airport = AirportService.read_airport_by_id(airport_id)
                to_city = airport.city
                view_flight = ViewFlightService.create_new_view_flight(flight_id, departure_time, arrival_time, airline,
                                                                       num_of_seats,
                                                                       num_of_available_tickets_first_class,
                                                                       num_of_available_tickets_second_class,
                                                                       price_first_class,
                                                                       price_second_class, from_city, to_city)

            view_flights = ViewFlightService.sort_view_flights_by_price()
            ViewFlightService.delete_view_flight()
            return view_flights[:3]
        except FlightNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
