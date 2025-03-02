# main.py

from fastapi import FastAPI
from controllers.booking_controller import router as booking_router

app = FastAPI()

# Include booking routes
app.include_router(booking_router, prefix="/bookings", tags=["Bookings"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Booking Microservice"}
