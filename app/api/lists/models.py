from mongoengine import (
    connection,
    Document,
    StringField,
    DateTimeField,
)
from datetime import datetime
import os

MONGO_CONNECTION_STRING = os.environ.get("MONGO_SRV")
connection.connect(host=MONGO_CONNECTION_STRING)


class List(Document):
    name = StringField(required=True)
    created_at = DateTimeField(default=datetime.utcnow)

    meta = {
        "indexes": ["name"],
        "ordering": ["-name"],
    }