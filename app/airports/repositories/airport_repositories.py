from app.airports.models import Airport
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.airports.exceptions import AirportNotFoundException

class AirportRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_airport(self, airport_name, city, country):
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
        airports = self.db.query(Airport).all()
        return airports

    def read_airport_by_id(self, airport_id):
        airport = self.db.query(Airport).filter(Airport.airport_id == airport_id).first()
        if airport is None:
            raise AirportNotFoundException(f"Airport with provided ID: {airport_id} not found.", 400)
        return airport

    def delete_airport(self, airport_id):
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


    def read_airport_by_name(self, airport_name):
        airport = self.db.query(Airport).filter(Airport.airport_name == airport_name).first()
        return airport