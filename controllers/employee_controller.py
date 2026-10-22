from fastapi import APIRouter
from fastapi import Depends
from repositories.database import get_db
from models.employee_model import EmployeeResponseModel
from services.employee_service import create_employee,get_employees,get_employee,update_employee,delete_employee
router=APIRouter()  
@router.post("/v1/employee",status_code=201)
def employee(emp:EmployeeResponseModel,db=Depends(get_db)):
    return create_employee(emp=emp,db=db)
@router.get("/v1/employee",status_code=200)
def employees(dept_id:int=None,role:str=None,db=Depends(get_db)):
    return get_employees(dept_id=dept_id,role=role,db=db)
@router.get("/v1/employee/{id}",status_code=200)
def employee(id:int,db=Depends(get_db)):
    return get_employee(id=id,db=db)
@router.put("/v1/employee/{id}",status_code=200)
def employee(id:int,emp:EmployeeResponseModel,db=Depends(get_db)):
    return update_employee(id=id,emp=emp,db=db)
@router.delete("/v1/employee/{id}",status_code=200)
def employee(id:int,db=Depends(get_db)):
    delete_employee(id=id,db=db) 