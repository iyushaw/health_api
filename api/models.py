from sqlalchemy import Column, DateTime, Integer, String, ForeignKey, Enum, Float, Text
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from database import Base

class Patient(Base):
    __tablename__ = 'patients'
    id = Column(Integer, primary_key=True, index=True)

class Doctor(Base):
    __tablename__ = 'doctors'
    id = Column(Integer, primary_key=True, index=True)\
    
class Appointment(Base):
    __tablename__ = 'appointments'
    id = Column(Integer, primary_key=True, index=True)