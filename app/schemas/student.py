from pydantic import BaseModel, field_validator
import re


class StudentCreate(BaseModel):

    name: str

    student_class: str

    percentage: float

    @field_validator("name")
    @classmethod
    def validate_name(cls, value):

        value = value.strip()

        if not value:
            raise ValueError(
                "Name cannot be empty"
            )

        if value.lower() in ["null", "none"]:
            raise ValueError(
                "Name cannot be null"
            )

        if not re.fullmatch(
            r"[A-Za-z ]+",
            value
        ):
            raise ValueError(
                "Name contains invalid characters"
            )

        return value

    @field_validator("student_class")
    @classmethod
    def validate_student_class(
        cls,
        value
    ):

        value = value.strip()

        if not value:
            raise ValueError(
                "Class name cannot be empty"
            )

        if value.lower() in ["null", "none"]:
            raise ValueError(
                "Class name cannot be null"
            )

        if not re.fullmatch(
            r"\d+[A-Za-z]",
            value
        ):
            raise ValueError(
                "Invalid class name. Expected format: Number followed by a letter (e.g. 7A, 8A, 10A)"
            )

        return value

    @field_validator("percentage")
    @classmethod
    def validate_percentage(
        cls,
        value
    ):

        if value < 0 or value > 100:
            raise ValueError(
                "Percentage must be between 0 and 100"
            )

        return value


class StudentResponse(BaseModel):

    id: str

    name: str

    student_class: str

    percentage: float