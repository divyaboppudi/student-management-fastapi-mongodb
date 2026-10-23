from bson import ObjectId


def is_valid_object_id(
    value: str
):

    return ObjectId.is_valid(
        value
    )