from models.employee_model import Employee,EmployeeResponseModel
from models.department_model import Department
from repositories.database import get_db
from fastapi import Depends
from sqlalchemy import select
from fastapi import HTTPException
def create_employee(emp:EmployeeResponseModel,db=Depends(get_db)):
    db_email=db.scalars(select(Employee).where(Employee.email==emp.email)).first()
    if db_email:
        raise HTTPException(status_code=400,detail="Email already existed")
    db_dept=db.get(Department,emp.dept_id)
    if db_dept is None:
        raise HTTPException(status_code=404,detail="Department not found")
    db_employee=Employee(ename=emp.ename,email=emp.email,role=emp.role,salary=emp.salary,dept_id=emp.dept_id)
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return {
    "msg":"Employee created successfully",
    "data":db_employee
    }
def get_employees(dept_id:int=None,role:str=None,db=Depends(get_db)):
    query=select(Employee)
    if dept_id is not None:
        query=query.where(Employee.dept_id==dept_id)
    if role is not None:
        query=query.where(Employee.role==role)
    db_emp=db.scalars(query).all()
    return {
        "data":db_emp
    }
def get_employee(id:int,db=Depends(get_db)):
    db_emp=db.get(Employee,id)
    if db_emp is None:
        raise HTTPException(status_code=404,detail="Employee Not found")
    return {"data":db_emp}
def update_employee(id:int,emp:EmployeeResponseModel,db=Depends(get_db)):
    db_emp=db.get(Employee,id)
    if db_emp is None:
        raise HTTPException(status_code=404,detail="Employee not found")
    db_dept=db.get(Department,emp.dept_id)
    if db_dept is None:
        raise HTTPException(status_code=404,detail="Department not found")
    db_email=db.scalars(select(Employee).where(Employee.email==emp.email,Employee.id!=id)).first()
    if db_email:
        raise HTTPException(status_code=400,detail="Email alreday exist")
    db_emp.ename=emp.ename
    db_emp.email=emp.email
    db_emp.role=emp.role
    db_emp.salary=emp.salary
    db_emp.dept_id=emp.dept_id
    db.commit()
    db.refresh(db_emp)
    return {
        "msg":"Employee updated successfully",
        "data":db_emp
    }
def delete_employee(id:int,db=Depends(get_db)):
    db_emp=db.get(Employee,id)
    if db_emp is None:
        raise HTTPException(status_code=404,detail="Employee not found")
    db.delete(db_emp)
    db.commit()
    return {
        "data":"Employee deleted successfully"
    }