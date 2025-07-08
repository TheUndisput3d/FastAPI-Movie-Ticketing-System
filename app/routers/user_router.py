from fastapi import APIRouter, Depends, HTTPException
from app.database.database import get_db
from sqlalchemy.orm import Session
from app.routers.auth_router import get_current_user
from app.models.models import Movie, Showtime, Booking
from app.schemas.schemas import BookingCreate, BookingOut, MovieOut, ShowTimeOut
from typing import List

router = APIRouter()

@router.get("/movies", response_model=List[MovieOut])
def get_movies(db: Session = Depends(get_db)):
    return db.query(Movie).all()

@router.get("/showtimes/{movie_id}", response_model=List[ShowTimeOut])
def get_showtimes(movie_id: int, db: Session = Depends(get_db)):
    return db.query(Showtime).filter(Showtime.movie_id == movie_id).all()

@router.post("/book", response_model=BookingOut)
def book_ticket(data: BookingCreate, db: Session = Depends(get_db), user = Depends(get_current_user)):
    showtime = db.query(Showtime).filter_by(id=data.showtime_id).first()
    if not showtime or showtime.available_seats < data.seats:
        raise HTTPException(status_code=400, detail="Not enough seats")
    showtime.available_seats -= data.seats
    booking = Booking(user_id=user.id, showtime_id=data.showtime_id, seats=data.seats)
    db.add(booking)
    db.commit()
    return booking

@router.delete("/cancel/{booking_id}")
def cancel_booking(booking_id: int, db: Session = Depends(get_db), user = Depends(get_current_user)):
    booking = db.query(Booking).filter_by(id=booking_id, user_id=user.id).first()
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    showtime = db.query(Showtime).get(booking.showtime_id)
    showtime.available_seats += booking.seats
    db.delete(booking)
    db.commit()
    return {"msg": "Booking cancelled"}