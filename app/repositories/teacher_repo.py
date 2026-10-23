from bson import ObjectId

from app.db.mongo import db


class TeacherRepository:

    def create_teacher(
        self,
        teacher_data
    ):

        teacher = {
            "name": teacher_data.name,
            "subject": teacher_data.subject,
            "class_name": teacher_data.class_name
        }

        result = db.teachers.insert_one(
            teacher
        )

        teacher["id"] = str(
            result.inserted_id
        )

        return teacher

    def get_teacher_by_details(
        self,
        name,
        subject,
        class_name
    ):

        return db.teachers.find_one(
            {
                "name": {
                    "$regex": f"^{name}$",
                    "$options": "i"
                },
                "subject": {
                    "$regex": f"^{subject}$",
                    "$options": "i"
                },
                "class_name": {
                    "$regex": f"^{class_name}$",
                    "$options": "i"
                }
            }
        )

    def get_teacher_by_id(
        self,
        teacher_id
    ):

        return db.teachers.find_one(
            {
                "_id": ObjectId(teacher_id)
            }
        )

    def get_students_by_teacher(
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
    def get_students_by_teacher_and_class(
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