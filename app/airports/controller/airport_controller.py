from app.airports.services import AirportService
from app.airports.exceptions import AirportExceptionCode, AirportNotFoundException
from fastapi import HTTPException, Response, status


class AirportController:

    @staticmethod
    def create_new_airport(airport_name: str, city: str, country: str):
        try:
            airport = AirportService.create_new_airport(airport_name, city, country)
            return airport
        except AirportExceptionCode as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_airports():
        airports = AirportService.read_all_airports()
        return airports

    @staticmethod
    def get_airport_by_id(airport_id: str):
        try:
            airport = AirportService.read_airport_by_id(airport_id)
            return airport
        except AirportNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_airport_by_id(airport_id: str):
        try:
            AirportService.delete_airport_by_id(airport_id)
            return Response(content=f"Airport with provided ID: {airport_id} deleted.", status_code=200)
        except AirportNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_airport_by_name(airport_name: str):
        airport = AirportService.read_airport_by_name(airport_name)
        if airport:
            return airport
        else:
            raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Airport with airport name {airport_name} does not exist",
        )

    @staticmethod
    def get_all_airports_with_city(city: str):
        airports = AirportService.read_all_airports_in_city(city)
        if bool(airports) is not False:
            return airports
        else:
            raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"There is no airport with airport city {city} ",
        )
