from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.database.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)
    is_admin = Column(Boolean, default=False)

    bookings = relationship("Booking", back_populates="user", cascade="all, delete")

class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True)
    title = Column(String)

    showtimes = relationship("Showtime", back_populates="movie", cascade="all, delete")

class Showtime(Base):
    __tablename__ = "showtimes"
    id = Column(Integer, primary_key=True)
    time = Column(String)
    available_seats = Column(Integer)
    movie_id = Column(Integer, ForeignKey("movies.id"))

    movie = relationship("Movie", back_populates="showtimes")
    bookings = relationship("Booking", back_populates="showtime", cascade="all, delete")

class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    showtime_id = Column(Integer, ForeignKey("showtimes.id"))
    seats = Column(Integer)

    user = relationship("User", back_populates="bookings")
    showtime = relationship("Showtime", back_populates="bookings")