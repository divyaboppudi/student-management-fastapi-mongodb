from fastapi import HTTPException
import re

from app.repositories.student_repo import (
    StudentRepository
)

from app.utils import (
    is_valid_object_id
)


class StudentService:

    def __init__(self):

        self.repo = StudentRepository()

    def create_student(
        self,
        student_data
    ):

        existing_student = (
            self.repo.get_student_by_details(
                student_data.name,
                student_data.student_class
            )
        )

        if existing_student:
            raise HTTPException(
                status_code=409,
                detail="Student already exists in this class"
            )

        return self.repo.create_student(
            student_data
        )

    def get_students_by_class(
        self,
        class_name
    ):

        if not class_name:
            raise HTTPException(
                status_code=400,
                detail="Class name is required"
            )

        class_name = class_name.strip()

        if not class_name:
            raise HTTPException(
                status_code=400,
                detail="Class name cannot be empty"
            )

        if class_name.lower() in [
            "null",
            "none"
        ]:
            raise HTTPException(
                status_code=400,
                detail="Class name cannot be null"
            )

        if not re.fullmatch(
            r"\d+[A-Za-z]",
            class_name
        ):
            raise HTTPException(
                status_code=400,
                detail="Invalid class name. Expected format: Number followed by a letter (e.g. 7A, 8A, 10A)"
            )

        class_name = class_name.upper()

        students = (
            self.repo.get_students_by_class(
                class_name
            )
        )

        if not students:
            raise HTTPException(
                status_code=404,
                detail="No students found"
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

    def get_student_by_id(
        self,
        student_id
    ):

        if not student_id:
            raise HTTPException(
                status_code=400,
                detail="Student ID is required"
            )

        if not is_valid_object_id(
            student_id
        ):
            raise HTTPException(
                status_code=400,
                detail="Invalid Student ID"
            )

        student = (
            self.repo.get_student_by_id(
                student_id
            )
        )

        if not student:
            raise HTTPException(
                status_code=404,
                detail="Student not found"
            )

        return {
            "id": str(student["_id"]),
            "name": student["name"],
            "student_class": student["student_class"],
            "percentage": student["percentage"]
        }

    def get_student_by_name_and_class(
        self,
        name,
        class_name
    ):

        if not name:
            raise HTTPException(
                status_code=400,
                detail="Name is required"
            )

        if not class_name:
            raise HTTPException(
                status_code=400,
                detail="Class name is required"
            )

        name = name.strip()

        class_name = class_name.strip()

        if not name:
            raise HTTPException(
                status_code=400,
                detail="Name cannot be empty"
            )

        if not class_name:
            raise HTTPException(
                status_code=400,
                detail="Class name cannot be empty"
            )

        class_name = class_name.upper()

        student = (
            self.repo.get_student_by_name_and_class(
                name,
                class_name
            )
        )

        if not student:
            raise HTTPException(
                status_code=404,
                detail="Student not found"
            )

        return {
            "id": str(student["_id"]),
            "name": student["name"],
            "student_class": student["student_class"],
            "percentage": student["percentage"]
        }
    def get_students_by_result(
        self,
        category
    ):

        if not category:
            raise HTTPException(
                status_code=400,
                detail="Category is required"
            )

        category = category.strip().lower()

        result_queries = {
            "distinction": {
                "percentage": {
                    "$gte": 75
                }
            },
            "firstclass": {
                "percentage": {
                    "$gte": 60,
                    "$lt": 75
                }
            },
            "secondclass": {
                "percentage": {
                    "$gte": 35,
                    "$lt": 60
                }
            },
            "fail": {
                "percentage": {
                    "$lt": 35
                }
            }
        }

        if category not in result_queries:
            raise HTTPException(
                status_code=400,
                detail="Invalid category. Allowed values: distinction, firstclass, secondclass, fail"
            )

        students = self.repo.get_students_by_result(
            result_queries[category]
        )

        if not students:
            raise HTTPException(
                status_code=404,
                detail="No students found"
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