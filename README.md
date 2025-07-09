# Movie Ticket Booking System

This project is a modular FastAPI backend for movie ticket booking. It supports user registration, authentication, role-based access, movie and showtime management, and ticket booking. The codebase is organized for maintainability and scalability.

---

## Setup and Installation Instructions

1. **Clone the Repository**
    ```
    git clone https://github.com/yourusername/movie-ticket-booking-system.git
    cd movie-ticket-booking-system
    ```

2. **Create and Activate a Virtual Environment**
    ```
    python -m venv venv
    # On Windows:
    venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3. **Install Dependencies**
    ```
    pip install -r requirements.txt
    ```

4. **Database Setup**
    - The SQLite database (`movie_booking.db`) is already included and seeded in the repository.
    - No further setup or seeding is required.

---

## Steps to Run the Application

1. **Start the FastAPI Server**
    ```
    uvicorn app.main:app --reload
    ```

2. **Access the API Documentation**
    - Open your browser and go to:  
      [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## User Registration and Authentication

Before using any endpoints, you must register and log in to obtain an access token.

### How to Register

There are two ways to register:

- **As a user:**  
  Send a POST request to `/auth/register` with the following JSON body:

{
"username": "your_username",
"password": "your_password",
"is_admin": false
}

Set `is_admin` to `false` for regular users.

- **As an admin:**  
Send a POST request to `/auth/register` with the following JSON body:

{
"username": "your_admin_username",
"password": "your_admin_password",
"is_admin": true
}

Set `is_admin` to `true` for admin accounts.

### How to Authorize

1. After registering, go to the top right of the Swagger UI and click the **Authorize** button.
2. Enter your registered username and password.
3. **Ignore** the `client_id` and `client_secret` fields; leave them blank.
4. Click "Authorize" to log in and obtain your access token.

- Once authorized:
- Regular users can access user endpoints.
- Admins can access both user and protected admin endpoints.

---

## API Endpoints

### Authentication

- **POST** `/auth/register`  
Register as a user or admin.

- **POST** `/auth/token`  
Login to obtain JWT token.

### User Endpoints

- **GET** `/user/movies`  
Get Movies

- **GET** `/user/showtimes/{movie_id}`  
Get Showtimes for a Movie

- **POST** `/user/book`  
Book Ticket

- **DELETE** `/user/cancel/{booking_id}`  
Cancel Booking

### Admin Endpoints

- **POST** `/admin/add_movie`  
Add Movie

- **DELETE** `/admin/delete_movie/{movie_id}`  
Delete Movie

- **POST** `/admin/add_showtime`  
Add Showtime

- **DELETE** `/admin/delete_showtime/{showtime_id}`  
Delete Showtime

- **GET** `/admin/movies-with-showtimes`  
Get All Movies With Showtimes

- **GET** `/admin/showtimes-with-bookings`  
Get All Showtimes With Bookings

---

## Python Version and Libraries Used

- **fastapi** — Web framework for building APIs  
- **uvicorn** — ASGI server to run FastAPI apps  
- **SQLAlchemy** — ORM for database management  
- **pydantic** — Data validation and serialization  
- **passlib** — Password hashing (bcrypt scheme)  
- **python-jose** — JWT token creation and verification  
- **python-multipart** — For handling form data (file uploads, etc.)  
- **bcrypt** — Password hashing backend used by passlib  
- **anyio** — Async concurrency library used by FastAPI/Starlette  
- **starlette** — ASGI toolkit used internally by FastAPI  



