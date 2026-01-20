from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
import pytz

from app.database import Base, engine
from app.models import User, FitnessClass, Booking
from app.schemas import UserCreate, UserLogin, ClassCreate, BookingCreate
from app.auth import hash_password, verify_password, create_access_token
from app.deps import get_db, get_current_user
from fastapi.security import OAuth2PasswordRequestForm



Base.metadata.create_all(bind=engine)

app = FastAPI(title="Fitness Studio API")

IST = pytz.timezone("Asia/Kolkata")

# ---------------- AUTH ----------------

@app.post("/signup")
def signup(data: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == data.email).first():
        raise HTTPException(400, "Email already exists")

    user = User(
        name=data.name,
        email=data.email,
        password=hash_password(data.password)
    )
    db.add(user)
    db.commit()
    return {"message": "User registered successfully"}



@app.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.email == form_data.username).first()

    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token({"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

# ---------------- CLASSES ----------------

@app.post("/classes")
def create_class(
    data: ClassCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    ist_time = data.dateTime.astimezone(IST)

    fitness_class = FitnessClass(
        name=data.name,
        date_time=ist_time,
        instructor=data.instructor,
        available_slots=data.availableSlots
    )
    db.add(fitness_class)
    db.commit()
    db.refresh(fitness_class)
    return fitness_class


@app.get("/classes")
def get_classes(db: Session = Depends(get_db)):
    # classes = db.query(FitnessClass).all()
    return db.query(FitnessClass).all()

# ---------------- BOOKINGS ----------------

@app.post("/book")
def book_class(
    data: BookingCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    fitness_class = db.query(FitnessClass).filter(
        FitnessClass.id == data.class_id
    ).first()

    if not fitness_class:
        raise HTTPException(404, "Class not found")

    if fitness_class.available_slots <= 0:
        raise HTTPException(400, "No slots available")

    booking = Booking(user_id=user.id, class_id=data.class_id)
    fitness_class.available_slots -= 1

    db.add(booking)
    db.commit()
    return {"message": "Class booked successfully"}

@app.get("/bookings")
def my_bookings(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return db.query(Booking).filter(Booking.user_id == user.id).all()
