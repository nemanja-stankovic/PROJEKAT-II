from app.airports.models import Airport
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.airports.exceptions import AirportNotFoundException

class AirportRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_airport(self, airport_name, city, country):
        """
        It creates an airport object, adds it to the database, commits the changes, and returns the airport object
        @param airport_name - The name of the airport
        @param city - The city where the airport is located.
        @param country - The country where the airport is located.
        @returns The airport object is being returned.
        """
        try:
            airport = Airport(airport_name=airport_name,city=city,country=country)
            self.db.add(airport)
            self.db.commit()
            self.db.refresh(airport)
            print(airport.airport_name)
            return airport
        except IntegrityError as e:
            raise e
        except Exception as e:
            raise e

    def read_all_airports(self):
        """
        It returns all the airports in the database
        @returns A list of all the airports in the database.
        """
        airports = self.db.query(Airport).all()
        return airports

    def read_airport_by_id(self, airport_id: str):
        """
        It returns an airport object from the database if it exists, otherwise it raises an exception
        @param {str} airport_id - str
        @returns The airport object is being returned.
        """
        airport = self.db.query(Airport).filter(Airport.airport_id == airport_id).first()
        if airport is None:
            raise AirportNotFoundException(f"Airport with provided ID: {airport_id} not found.", 400)
        return airport

    def delete_airport(self, airport_id: str):
        """
        It deletes an airport from the database
        @param {str} airport_id - str
        @returns True
        """
        try:
            airport = self.db.query(Airport).filter(Airport.airport_id == airport_id).first()
            if airport is None:
                raise AirportNotFoundException(f"Airport with provided ID: {airport_id} not found.", 400)
            self.db.delete(airport)
            self.db.commit()
            # self.db.refresh(airport)
            return True
        except Exception as e:
            raise e


    def read_airport_by_name(self, airport_name: str):
        """
        It returns the first airport in the database that matches the given airport name
        @param {str} airport_name - str
        @returns The first airport with the name airport_name.
        """
        airport = self.db.query(Airport).filter(Airport.airport_name == airport_name).first()
        return airport

    def read_airports_by_city(self, city: str):
        """
        > This function returns a list of airports in a given city
        @param {str} city - str
        @returns A list of airports
        """
        airports = self.db.query(Airport).filter(Airport.city == city).all()
        return airports

    def read_airports_ids_by_city(self, city: str):
        """
        It returns a list of airport ids for a given city
        @param {str} city - str
        @returns A list of airport ids
        """
        airports = self.db.query(Airport).filter(Airport.city == city).all()
        airport_ids=[]
        for airport in airports:
            airport_id = airport.airport_id
            airport_ids.append(airport_id)
        return airport_ids
