# utils/validation.py

from pydantic import BaseModel, Field, validator
from datetime import datetime

class VendorDetails(BaseModel):
    vendor_name: str
    vendor_id: str

class Booking(BaseModel):
    booking_id: str = Field(..., description="Unique identifier for booking")
    customer_name: str = Field(..., description="Name of the customer")
    booking_date: str = Field(..., description="Date of booking (YYYY-MM-DD)")
    amount: float = Field(..., gt=0, description="Booking amount")
    vendor_details: VendorDetails

    @validator("booking_date")
    def validate_booking_date(cls, value):
        try:
            # Normalize date format to YYYY-MM-DD
            normalized_date = datetime.strptime(value, "%Y-%m-%d").date()
            return normalized_date.isoformat()
        except ValueError:
            raise ValueError("booking_date must be in YYYY-MM-DD format")
