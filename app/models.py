from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    bookings = relationship("Booking", back_populates="user")


class FitnessClass(Base):
    __tablename__ = "classes"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    date_time = Column(DateTime)
    instructor = Column(String)
    available_slots = Column(Integer)


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    class_id = Column(Integer, ForeignKey("classes.id"))

    user = relationship("User", back_populates="bookings")
