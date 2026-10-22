from fastapi import Depends
from repositories.database import get_db
from models.department_model import Department,DepartmentResponseModel
from models.employee_model import Employee,EmployeeResponseModel
from sqlalchemy import select
from fastapi import HTTPException
def create_department(dept:DepartmentResponseModel,db=Depends(get_db)):
    db_dept=db.scalars(select(Department).where(Department.dname==dept.dname)).first()
    if db_dept:
        raise HTTPException(status_code=400,detail="Department name already exists")
    if dept.budget<=0 :
        raise HTTPException(status_code=400,detail="Budget must be greater than 0")
    db_budget=db.scalars(select(Department).where(Department.budget==dept.budget)).first()
    if db_budget:
        raise HTTPException(status_code=400,detail="Budget already allocated")
    #db_head=db.get(Employee,dept.head_employee_id)
    #if db_head is None:
     # raise HTTPException(status_code=404,detail="Head employee not found")
    db_department=Department(dname=dept.dname,budget=dept.budget,head_employee_id=dept.head_employee_id,is_deleted=dept.is_deleted)
    db.add(db_department)
    db.commit()
    db.refresh(db_department)
    return{
        "msg":"department is created",
        "data":db_department
    }
def get_departments(skip:int,limit:int,db=Depends(get_db)):
    db_department=db.scalars(select(Department).where(Department.is_deleted==False).offset(skip).limit(limit)).all()
    return{"msg":db_department}
def get_department(id:int,db=Depends(get_db)):
    db_department=db.get(Department,id)
    if db_department is None:
        raise HTTPException(status_code=404,detail="Department not found")
    return{"data":db_department}
def update_department(id:int,dept:DepartmentResponseModel,db=Depends(get_db)):
    db_department=db.get(Department,id)
    if db_department is None:
        raise HTTPException(status_code=404,detail="Department not found")
    db_dept=db.scalars(select(Department).where(Department.dname==dept.dname,Department.id!=id)).first()
    if db_dept:
        raise HTTPException(status_code=400,detail="Department already existed")
    if dept.budget<=0:
        raise HTTPException(status_code=400,detail="Budget must be greater than 0")
    db_budget=db.scalars(select(Department).where(Department.budget==dept.budget,Department.id!=id)).first()
    if db_budget:
        raise HTTPException(status_code=400,detail="Budget already allocated")
    #db_head=db.get(Employee,dept.head_employee_id)
    #if db_head is None:
     #  raise HTTPException(status_code=404,detail="Head employee not found")
    db_department.dname=dept.dname
    db_department.budget=dept.budget
    db_department.head_employee_id=dept.head_employee_id
    db_department.is_deleted=dept.is_deleted
    db.commit()
    db.refresh(db_department)
    return{
        "msg":"updated successfully",
        "data":db_department
           }
def delete_department(id:int,db=Depends(get_db)):
    db_department=db.get(Department,id)
    if db_department is None:
        raise HTTPException(status_code=404,detail="Department not found")
    db_employee=db.scalars(select(Employee).where(Employee.dept_id==id)).first()
    if db_employee: 
        raise HTTPException(status_code=400,detail="Cannot delete department.Employees are assigned.")
    db_department.is_deleted=True
    db.commit()
    db.refresh(db_department)
    return{
        "msg":"Department deleted successfully"
    }