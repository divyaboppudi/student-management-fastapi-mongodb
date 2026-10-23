from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from app.api.students import (
    router as student_router
)

from app.api.teachers import (
    router as teacher_router
)

from app.exceptions import (
    validation_exception_handler
)


app = FastAPI(
    title="Student Management API - MongoDB"
)

# Student APIs
app.include_router(
    student_router
)

# Teacher APIs
app.include_router(
    teacher_router
)

# Global Validation Handler
app.add_exception_handler(
    RequestValidationError,
    validation_exception_handler
)


@app.get("/")
def home():

    return {
        "message": "MongoDB Connection Successful"
    }