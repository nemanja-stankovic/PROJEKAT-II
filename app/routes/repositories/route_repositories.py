# from app.routes.models import Route
# from sqlalchemy.exc import IntegrityError
# from sqlalchemy.orm import Session
# from app.routes.exceptions import RouteNotFoundException
#
# class RouteRepository:
#
#     def __init__(self, db: Session):
#         self.db = db
#
#     def create_route(self, from_airport_id, to_airport_id):
#         try:
#             route = Route(from_airport_id=from_airport_id,to_airport_id=to_airport_id)
#             self.db.add(route)
#             self.db.commit()
#             self.db.refresh(route)
#             return route
#         except IntegrityError as e:
#             raise e
#         except Exception as e:
#             raise e
#
#     def read_all_routes(self):
#         airports = self.db.query(Airport).all()
#         return airports
#
#     def read_airport_by_id(self, airport_id):
#         airport = self.db.query(Airport).filter(Airport.airport_ID == airport_id).first()
#         if airport is None:
#             raise AirportNotFoundException(f"Airport with provided ID: {airport_id} not found.", 400)
#         return airport
#
#     def delete_airport(self, airport_id):
#         try:
#             airport = self.db.query(Airport).filter(Airport.airport_ID == airport_id).first()
#             if airport is None:
#                 raise AirportNotFoundException(f"Airport with provided ID: {airport_id} not found.", 400)
#             self.db.delete(airport)
#             self.db.commit()
#             # self.db.refresh(airport)
#             return True
#         except Exception as e:
#             raise e
#
#
#     def read_airport_by_name(self, airport_name):
#         airport = self.db.query(Airport).filter(Airport.airport_name == airport_name).first()
#         return airport