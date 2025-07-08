from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.models import Movie, Showtime
from app.schemas.schemas import MovieBase, ShowTimeBase, MovieOut, ShowTimeOut
from app.routers.auth_router import get_current_user
from app.database.database import get_db

router = APIRouter()

def is_admin(user):
    if not user.is_admin:
        raise HTTPException(status_code=403, detail="Admins only")
    return True

@router.post("/add_movie", response_model=MovieOut)
def add_movie(movie: MovieBase, db: Session = Depends(get_db), user = Depends(get_current_user)):
    is_admin(user)
    new_movie = Movie(title=movie.title)
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)
    return new_movie

@router.delete("/delete_movie/{movie_id}")
def delete_movie(movie_id: int, db: Session = Depends(get_db), user = Depends(get_current_user)):
    is_admin(user)
    movie = db.query(Movie).get(movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    db.delete(movie)
    db.commit()
    return {"msg": "Movie deleted"}

@router.post("/add_showtime", response_model=ShowTimeOut)
def add_showtime(showtime: ShowTimeBase, db: Session = Depends(get_db), user = Depends(get_current_user)):
    is_admin(user)
    new_showtime = Showtime(**showtime.dict())
    db.add(new_showtime)
    db.commit()
    db.refresh(new_showtime)
    return new_showtime

@router.delete("/delete_showtime/{showtime_id}")
def delete_showtime(showtime_id: int, db: Session = Depends(get_db), user = Depends(get_current_user)):
    is_admin(user)
    st = db.query(Showtime).get(showtime_id)
    if not st:
        raise HTTPException(status_code=404, detail="Showtime not found")
    db.delete(st)
    db.commit()
    return {"msg": "Showtime deleted"}

@router.get("/movies-with-showtimes", response_model=list[MovieOut])
def get_all_movies_with_showtimes(db: Session = Depends(get_db), user = Depends(get_current_user)):
    is_admin(user)
    return db.query(Movie).all()

@router.get("/showtimes-with-bookings", response_model=list[ShowTimeOut])
def get_all_showtimes_with_bookings(db: Session = Depends(get_db), user = Depends(get_current_user)):
    is_admin(user)
    return db.query(Showtime).all()