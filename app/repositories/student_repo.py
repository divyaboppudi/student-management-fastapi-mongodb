from bson import ObjectId

from app.db.mongo import db


class StudentRepository:

    def create_student(
        self,
        student_data
    ):

        student = {
            "name": student_data.name,
            "student_class": student_data.student_class,
            "percentage": student_data.percentage
        }

        result = db.students.insert_one(
            student
        )

        student["id"] = str(
            result.inserted_id
        )

        return student

    def get_student_by_details(
        self,
        name,
        student_class
    ):

        return db.students.find_one(
            {
                "name": {
                    "$regex": f"^{name}$",
                    "$options": "i"
                },
                "student_class": {
                    "$regex": f"^{student_class}$",
                    "$options": "i"
                }
            }
        )

    def get_students_by_class(
        self,
        class_name
    ):

        return list(
            db.students.find(
                {
                    "student_class": {
                        "$regex": f"^{class_name}$",
                        "$options": "i"
                    }
                }
            )
        )

    def get_student_by_id(
        self,
        student_id
    ):

        return db.students.find_one(
            {
                "_id": ObjectId(student_id)
            }
        )

    def get_student_by_name_and_class(
        self,
        name,
        class_name
    ):

        return db.students.find_one(
            {
                "name": {
                    "$regex": f"^{name}$",
                    "$options": "i"
                },
                "student_class": {
                    "$regex": f"^{class_name}$",
                    "$options": "i"
                }
            }
        )

    def get_students_by_result(
        self,
        query
    ):

        return list(
            db.students.find(
                query
            )
        )