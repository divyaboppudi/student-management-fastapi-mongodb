from fastapi import HTTPException

from app.repositories.teacher_repo import (
    TeacherRepository
)

from app.utils import (
    is_valid_object_id
)


class TeacherService:

    def __init__(self):

        self.repo = TeacherRepository()

    def create_teacher(
        self,
        teacher_data
    ):

        existing_teacher = (
            self.repo.get_teacher_by_details(
                teacher_data.name,
                teacher_data.subject,
                teacher_data.class_name
            )
        )

        if existing_teacher:
            raise HTTPException(
                status_code=409,
                detail="Teacher already exists for this subject and class"
            )

        return self.repo.create_teacher(
            teacher_data
        )

    def get_teacher_by_id(
        self,
        teacher_id
    ):

        if not teacher_id:
            raise HTTPException(
                status_code=400,
                detail="Teacher ID is required"
            )

        if not is_valid_object_id(
            teacher_id
        ):
            raise HTTPException(
                status_code=400,
                detail="Invalid Teacher ID"
            )

        teacher = self.repo.get_teacher_by_id(
            teacher_id
        )

        if not teacher:
            raise HTTPException(
                status_code=404,
                detail="Teacher not found"
            )

        return {
            "id": str(teacher["_id"]),
            "name": teacher["name"],
            "subject": teacher["subject"],
            "class_name": teacher["class_name"]
        }

    def get_students_under_teacher(
        self,
        teacher_id
    ):

        if not teacher_id:
            raise HTTPException(
                status_code=400,
                detail="Teacher ID is required"
            )

        if not is_valid_object_id(
            teacher_id
        ):
            raise HTTPException(
                status_code=400,
                detail="Invalid Teacher ID"
            )

        teacher = self.repo.get_teacher_by_id(
            teacher_id
        )

        if not teacher:
            raise HTTPException(
                status_code=404,
                detail="Teacher not found"
            )

        students = self.repo.get_students_by_teacher(
            teacher["class_name"]
        )

        if not students:
            raise HTTPException(
                status_code=404,
                detail="No students found under this teacher"
            )

        response = []

        for student in students:

            response.append(
                {
                    "id": str(student["_id"]),
                    "name": student["name"],
                    "student_class": student["student_class"],
                    "percentage": student["percentage"]
                }
            )

        return response
    def get_students_by_teacher_and_class(
        self,
        teacher_id,
        class_name
    ):

        if not teacher_id:
            raise HTTPException(
                status_code=400,
                detail="Teacher ID is required"
            )

        if not class_name:
            raise HTTPException(
                status_code=400,
                detail="Class name is required"
            )

        if not is_valid_object_id(
            teacher_id
        ):
            raise HTTPException(
                status_code=400,
                detail="Invalid Teacher ID"
            )

        teacher = self.repo.get_teacher_by_id(
            teacher_id
        )

        if not teacher:
            raise HTTPException(
                status_code=404,
                detail="Teacher not found"
            )

        class_name = class_name.strip().upper()

        if teacher["class_name"].upper() != class_name:
            raise HTTPException(
                status_code=400,
                detail=f"Teacher is not assigned to class {class_name}"
            )

        students = (
            self.repo.get_students_by_teacher_and_class(
                class_name
            )
        )

        if not students:
            raise HTTPException(
                status_code=404,
                detail="No students found for the given class"
            )

        response = []

        for student in students:

            response.append(
                {
                    "id": str(student["_id"]),
                    "name": student["name"],
                    "student_class": student["student_class"],
                    "percentage": student["percentage"]
                }
            )

        return response