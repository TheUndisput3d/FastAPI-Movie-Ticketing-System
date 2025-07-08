from sqlalchemy.orm import Session
from app.database.database import SessionLocal
from app.models.models import Movie, Showtime
import random

db: Session = SessionLocal()

movie_titles = [
    "Inception", "Interstellar", "The Matrix", "Parasite", "The Dark Knight",
    "Everything Everywhere All at Once", "Knives Out", "Dune", "The Godfather",
    "Spirited Away", "La La Land", "Whiplash", "Tenet", "The Grand Budapest Hotel",
    "Blade Runner 2049", "Arrival", "Coco", "Joker", "1917", "Ford v Ferrari",
    "The Prestige", "Oppenheimer", "Her", "Avatar", "The Social Network",
    "The Imitation Game", "Black Panther", "WALL·E", "The Revenant", "The Martian",
    "Get Out", "The Irishman", "The Truman Show", "The Shawshank Redemption",
    "Prisoners", "The Wolf of Wall Street", "Fight Club", "No Country for Old Men",
    "Shutter Island", "Moonlight", "Jojo Rabbit", "Lady Bird", "Sound of Metal",
    "Nomadland", "Barbie", "John Wick", "A Quiet Place", "Doctor Strange", "Deadpool"
]

show_times = ["10:00 AM", "1:00 PM", "4:00 PM", "7:00 PM", "9:30 PM"]

for title in movie_titles:
    movie = Movie(title=title)
    db.add(movie)
    db.flush()  # Flush to get movie.id

    chosen_times = random.sample(show_times, k=3)
    for time in chosen_times:
        showtime = Showtime(
            time=time,
            available_seats=random.randint(20, 100),
            movie_id=movie.id
        )
        db.add(showtime)

db.commit()
db.close()
print("🎉 Seeded database with popular movies and showtimes!")