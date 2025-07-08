from pydantic import BaseModel
from typing import List, Optional

# User Schemas
class UserCreate(BaseModel):
    username: str
    password: str
    is_admin: bool = False

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class BookingOut(BaseModel):
    id: int
    showtime_id: int
    seats: int

    class Config:
        orm_mode = True

class UserOut(BaseModel):
    id: int
    username: str
    bookings: List[BookingOut] = []

    class Config:
        orm_mode = True

# Movie & Showtime
class MovieBase(BaseModel):
    title: str

class MovieOut(MovieBase):
    id: int
    class Config:
        orm_mode = True

class ShowTimeBase(BaseModel):
    time: str
    available_seats: int
    movie_id: int

class ShowTimeOut(BaseModel):
    id: int
    time: str
    available_seats: int
    movie_id: int
    bookings: List[BookingOut] = []

    class Config:
        orm_mode = True

# Booking
class BookingCreate(BaseModel):
    showtime_id: int
    seats: int