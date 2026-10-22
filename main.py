from fastapi import FastAPI
from repositories.database import Base,engine
from models.department_model import Department
from models.employee_model import Employee
from controllers.department_controller import router as dept_router
from controllers.employee_controller import router as emp_router
app=FastAPI()
Base.metadata.create_all(bind=engine)
app.include_router(dept_router)
app.include_router(emp_router)