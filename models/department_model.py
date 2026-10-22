from repositories.database import Base
from sqlalchemy import Column,Integer,String,Boolean
from pydantic import BaseModel
from sqlalchemy.orm import relationship
#orm model-->Department
class Department(Base):
    __tablename__="departments"
    id=Column(Integer,primary_key=True)
    dname=Column(String(100))
    budget=Column(Integer)
    head_employee_id=Column(Integer)
    is_deleted=Column(Boolean,default=False)
    employees=relationship("Employee",back_populates="department")
#pydantic model
class DepartmentResponseModel(BaseModel):
    dname:str
    budget:int
    head_employee_id:int
    is_deleted:bool