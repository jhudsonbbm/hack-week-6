from datetime import datetime
from bson.objectid import ObjectId, InvalidId


class PydanticOID(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        try:
            ObjectId(str(v))
        except InvalidId:
            raise ValueError("Not a valid ObjectId")
        return str(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(
            title="ObjectID",
            description="24 character hex string.",
            example="1234dead1234beef1234cafe",
        )