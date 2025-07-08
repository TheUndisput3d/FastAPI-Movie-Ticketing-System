from app.database.database import SessionLocal
from app.models.models import User, Movie, Showtime, Booking

db = SessionLocal()

users = db.query(User).all()
movies = db.query(Movie).all()
showtimes = db.query(Showtime).all()
bookings = db.query(Booking).all()

print("Users:", [u.username for u in users])
print("Movies:", [m.title for m in movies])
print("Showtimes:", [f"{s.time} for movie_id {s.movie_id}" for s in showtimes])
print("Bookings:", [f"user {b.user_id} → showtime {b.showtime_id}" for b in bookings])

db.close()