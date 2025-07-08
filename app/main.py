from fastapi import FastAPI
from app.database.database import Base, engine
from app.routers import auth_router, user_router, admin_router

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="🎬 Movie Ticket Booking System")

# Mount routers
app.include_router(auth_router.router, prefix="/auth", tags=["Authentication"])
app.include_router(user_router.router, prefix="/user", tags=["User"])
app.include_router(admin_router.router, prefix="/admin", tags=["Admin"])