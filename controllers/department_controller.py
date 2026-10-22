from fastapi import APIRouter
from fastapi import Depends
from repositories.database import get_db
from models.department_model import DepartmentResponseModel
from services.department_service import create_department,get_departments,get_department,update_department,delete_department
router=APIRouter()
@router.post("/v1/department",status_code=201)
def department(dept:DepartmentResponseModel,db=Depends(get_db)):
    return create_department(dept=dept,db=db)
@router.get("/v1/department",status_code=200)
def departments(skip:int=0,limit:int=5,db=Depends(get_db)):
    return get_departments(skip=skip,limit=limit,db=db)
@router.get("/v1/department/{id}",status_code=200)
def department(id:int,db=Depends(get_db)):
    return get_department(id=id,db=db)
@router.put("/v1/department/{id}")
def department(id:int,dept:DepartmentResponseModel,db=Depends(get_db)):
    return update_department(id=id,dept=dept,db=db)
@router.delete("/v1/department/{id}",status_code=200)
def department(id:int,db=Depends(get_db)):
    return delete_department(id=id,db=db)