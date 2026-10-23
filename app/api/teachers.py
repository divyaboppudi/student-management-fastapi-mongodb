from fastapi import APIRouter
from fastapi import Query

from app.schemas.teacher import (
    TeacherCreate,
    TeacherResponse
)

from app.schemas.student import (
    StudentResponse
)

from app.services.teacher_service import (
    TeacherService
)


router = APIRouter()

service = TeacherService()


@router.post(
    "/teachers",
    response_model=TeacherResponse
)
def create_teacher(
    teacher: TeacherCreate
):

    return service.create_teacher(
        teacher
    )


@router.get(
    "/teachers/students",
    response_model=list[StudentResponse]
)
def get_students_under_teacher(
    teacher_id: str = Query(
        ...,
        description="Teacher ID"
    )
):

    return service.get_students_under_teacher(
        teacher_id
    )


@router.get(
    "/teachers/students/filter",
    response_model=list[StudentResponse]
)
def get_students_by_teacher_and_class(
    teacher_id: str = Query(
        ...,
        description="Teacher ID"
    ),
    class_name: str = Query(
        ...,
        description="Class name"
    )
):

    return service.get_students_by_teacher_and_class(
        teacher_id,
        class_name
    )


@router.get(
    "/teachers/{teacher_id}",
    response_model=TeacherResponse
)
def get_teacher_by_id(
    teacher_id: str
):

    return service.get_teacher_by_id(
        teacher_id
    )