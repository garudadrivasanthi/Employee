from repositories.database import Base
from sqlalchemy import Column,Integer,String,Boolean,ForeignKey
from pydantic import BaseModel,field_validator
from sqlalchemy.orm import relationship
class Employee(Base):
    __tablename__="employees"
    id=Column(Integer,primary_key=True)
    ename=Column(String(100))
    email=Column(String(100))
    role=Column(String(100))
    salary=Column(Integer)
    dept_id=Column(Integer,ForeignKey("departments.id"))
    department=relationship("Department",back_populates="employees")
class EmployeeResponseModel(BaseModel):
    ename:str
    email:str
    role:str
    salary:int
    dept_id:int
    @field_validator("salary")
    @classmethod
    def validate_salary(cls,value):
        if value<30000:
            raise ValueError("Salary must be at least 30000")
        return value
    @field_validator("email")
    @classmethod
    def validate_email(cls,email):
        if not email.endswith("@company.com"):
            raise ValueError("Email must end with @company.com")
        return email