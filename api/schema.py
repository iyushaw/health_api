from pydantic import BaseModel
from typing import Optional

# Create Schema
class CreatePatientSchema(BaseModel):
    pass

    class Config:
        from_attributes = True

class CreateDoctorSchema(BaseModel):
    pass

    class Config:
        from_attributes = True

class CreateAppointmentSchema(BaseModel):
    pass

    class Config:
        from_attributes = True

# Get Objects 
class PatientSchema(BaseModel):
    pass

    class Config:
        from_attributes = True

class DoctorSchema(BaseModel):
    pass

    class Config:
        from_attributes = True

class AppointmentSchema(BaseModel):
    pass

    class Config:
        from_attributes = True

# Update Schemas
class PatientSchema(BaseModel):
    pass

    class Config:
        from_attributes = True

class DoctorSchema(BaseModel):
    pass

class AppointmentSchema(BaseModel):
    pass