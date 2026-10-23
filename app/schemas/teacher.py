from pydantic import BaseModel, field_validator
import re


class TeacherCreate(BaseModel):

    name: str

    subject: str

    class_name: str

    @field_validator("name")
    @classmethod
    def validate_name(
        cls,
        value
    ):

        value = value.strip()

        if not value:
            raise ValueError(
                "Name cannot be empty"
            )

        if value.lower() in [
            "null",
            "none"
        ]:
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

    @field_validator("subject")
    @classmethod
    def validate_subject(
        cls,
        value
    ):

        value = value.strip()

        if not value:
            raise ValueError(
                "Subject cannot be empty"
            )

        if value.lower() in [
            "null",
            "none"
        ]:
            raise ValueError(
                "Subject cannot be null"
            )

        if not re.fullmatch(
            r"[A-Za-z ]+",
            value
        ):
            raise ValueError(
                "Subject contains invalid characters"
            )

        return value

    @field_validator("class_name")
    @classmethod
    def validate_class_name(
        cls,
        value
    ):

        value = value.strip()

        if not value:
            raise ValueError(
                "Class name cannot be empty"
            )

        if value.lower() in [
            "null",
            "none"
        ]:
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

        return value.upper()


class TeacherResponse(BaseModel):

    id: str

    name: str

    subject: str

    class_name: str