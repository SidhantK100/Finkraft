# models/booking_model.py

from pymongo import MongoClient
from config import MONGO_URI, DATABASE_NAME

client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]
bookings_collection = db["bookings"]

# Insert a new booking
def create_booking(booking_data):
    bookings_collection.insert_one(booking_data)

# Get bookings with optional filters
def get_bookings(filter_query=None):
    if filter_query is None:
        filter_query = {}
    return list(bookings_collection.find(filter_query, {"_id": 0}))

# Get a single booking by ID
def get_booking_by_id(booking_id):
    return bookings_collection.find_one({"booking_id": booking_id}, {"_id": 0})

# Delete a booking by ID
def delete_booking_by_id(booking_id):
    result = bookings_collection.delete_one({"booking_id": booking_id})
    return result.deleted_count > 0
