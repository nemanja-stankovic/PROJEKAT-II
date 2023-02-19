import uvicorn
from fastapi import FastAPI
from starlette.responses import RedirectResponse

from app.db.database import engine, Base
from app.airports.routes import airport_router
from app.users.routes import user_router
from app.flight_routes.routes import flight_route_router
from app.flights.routes import flight_router
from app.tickets.routes import ticket_router
Base.metadata.create_all(bind=engine)


def init_app():
    app = FastAPI()
    app.include_router(airport_router)
    app.include_router(flight_route_router)
    app.include_router(user_router)
    app.include_router(flight_router)
    app.include_router(ticket_router)
    return app


app = init_app()


# @app.get("/", include_in_schema=False)
# def hello_world():
#     return RedirectResponse('/docs')


if __name__ == "__main__":
    uvicorn.run(app)
