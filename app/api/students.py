from fastapi import APIRouter
from fastapi import Query

from app.schemas.student import (
    StudentCreate,
    StudentResponse
)

from app.services.student_service import (
    StudentService
)


router = APIRouter()

service = StudentService()


@router.post(
    "/students",
    response_model=StudentResponse
)
def create_student(
    student: StudentCreate
):

    return service.create_student(
        student
    )


@router.get(
    "/students",
    response_model=list[StudentResponse]
)
def get_students_by_class(
    class_name: str = Query(
        ...,
        description="Class name (e.g. 7A, 8A, 10A)"
    )
):

    return service.get_students_by_class(
        class_name
    )


@router.get(
    "/students/result",
    response_model=list[StudentResponse]
)
def get_students_by_result(
    category: str = Query(
        ...,
        description="distinction, firstclass, secondclass, fail"
    )
):

    return service.get_students_by_result(
        category
    )


@router.get(
    "/student",
    response_model=StudentResponse
)
def get_student_by_name_and_class(
    name: str = Query(
        ...,
        description="Student name"
    ),
    class_name: str = Query(
        ...,
        description="Class name (e.g. 7A, 8A, 10A)"
    )
):

    return service.get_student_by_name_and_class(
        name,
        class_name
    )


@router.get(
    "/students/{student_id}",
    response_model=StudentResponse
)
def get_student_by_id(
    student_id: str
):

    return service.get_student_by_id(
        student_id
    )