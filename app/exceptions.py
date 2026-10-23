from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi import Request


async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
):
    error = exc.errors()[0]

    error_type = error.get("type")
    error_location = error.get("loc", [])

    if error_type == "missing":

        field_name = error_location[-1]

        friendly_names = {
            "name": "Name",
            "student_class": "Class name",
            "percentage": "Percentage"
        }

        field_display_name = friendly_names.get(
            field_name,
            field_name.replace("_", " ").title()
        )

        return JSONResponse(
            status_code=400,
            content={
                "detail": f"{field_display_name} is required"
            }
        )

    error_message = error.get("msg")

    if error_message.startswith("Value error, "):
        error_message = error_message.replace(
            "Value error, ",
            ""
        )

    return JSONResponse(
        status_code=400,
        content={
            "detail": error_message
        }
    )