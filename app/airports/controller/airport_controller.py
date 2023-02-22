from app.airports.services import AirportService
""""This class is responsible for controlling the airport"""
from app.airports.exceptions import AirportExceptionCode, AirportNotFoundException
from fastapi import HTTPException, Response, status


class AirportController:
    """"This class is responsible for controlling the airport."""""
    @staticmethod
    def create_new_airport(airport_name: str, city: str, country: str):
        """
        It creates a new airport.

        :param airport_name: str, city: str, country: str
        :type airport_name: str
        :param city: str, country: str
        :type city: str
        :param country: str - The country where the airport is located
        :type country: str
        :return: The airport object is being returned.
        """
        try:
            airport = AirportService.create_new_airport(airport_name, city, country)
            return airport
        except AirportExceptionCode as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_all_airports():
        """
        It returns a list of all airports in the database
        :return: A list of all airports
        """
        airports = AirportService.read_all_airports()
        return airports

    @staticmethod
    def get_airport_by_id(airport_id: str):
        """
        It returns the airport object with the given airport_id.

        :param airport_id: str
        :type airport_id: str
        :return: The airport object is being returned.
        """
        try:
            airport = AirportService.read_airport_by_id(airport_id)
            return airport
        except AirportNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def delete_airport_by_id(airport_id: str):
        """
        It deletes an airport by its ID.

        :param airport_id: str - the ID of the airport to be deleted
        :type airport_id: str
        :return: Response object
        """
        try:
            AirportService.delete_airport_by_id(airport_id)
            return Response(content=f"Airport with provided ID: {airport_id} deleted.", status_code=200)
        except AirportNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message) from e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) from e

    @staticmethod
    def get_airport_by_name(airport_name: str):
        """
        It takes in an airport name, and returns the airport object if it exists, otherwise it raises an exception

        :param airport_name: str - This is the name of the airport that we want to get
        :type airport_name: str
        :return: The airport object is being returned.
        """
        airport = AirportService.read_airport_by_name(airport_name)
        if airport:
            return airport
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Airport with airport name {airport_name} does not exist")

    @staticmethod
    def get_all_airports_with_city(city: str):
        """
        It returns all airports in a given city

        :param city: str - This is the city of the airport you want to search for
        :type city: str
        :return: A list of airports with the city name
        """
        airports = AirportService.read_all_airports_in_city(city)
        if bool(airports) is not False:
            return airports
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"There is no airport with airport city {city} ")
