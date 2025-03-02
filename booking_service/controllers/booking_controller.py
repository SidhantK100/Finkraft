# controllers/booking_controller.py

from fastapi import APIRouter, HTTPException, Query
from models.booking_model import (
    create_booking,
    get_bookings,
    get_booking_by_id,
    delete_booking_by_id
)
from utils.validation import Booking

router = APIRouter()

# POST /bookings - create a new booking
@router.post("/")
def add_booking(booking: Booking):
    existing_booking = get_booking_by_id(booking.booking_id)
    if existing_booking:
        raise HTTPException(status_code=400, detail="Booking ID already exists")
    create_booking(booking.dict())
    return {"status": "success", "message": "Booking added successfully"}

# GET /bookings - retrieve bookings with optional filters
@router.get("/")
def retrieve_bookings(
    date: str = Query(None, description="Filter by booking date (YYYY-MM-DD)"),
    vendor: str = Query(None, description="Filter by vendor name")
):
    query = {}
    if date:
        query["booking_date"] = date
    if vendor:
        query["vendor_details.vendor_name"] = vendor
    bookings = get_bookings(query)
    return {"status": "success", "data": bookings}

# GET /bookings/{id} - retrieve booking by ID
@router.get("/{booking_id}")
def retrieve_booking_by_id(booking_id: str):
    booking = get_booking_by_id(booking_id)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return {"status": "success", "data": booking}

# DELETE /bookings/{id} - delete booking by ID
@router.delete("/{booking_id}")
def remove_booking(booking_id: str):
    deleted = delete_booking_by_id(booking_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Booking not found or already deleted")
    return {"status": "success", "message": "Booking deleted successfully"}
