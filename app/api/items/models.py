from bson.objectid import ObjectId
from app.api.lists.models import List
from mongoengine import (
    connection,
    Document,
    StringField,
    BooleanField,
    DateTimeField,
    ReferenceField,
    CASCADE
)
from datetime import datetime
import os

MONGO_CONNECTION_STRING = os.environ.get('MONGO_SRV')
connection.connect(host=MONGO_CONNECTION_STRING)


class Item(Document):
    title = StringField(required=True)
    description = StringField(max_length=200)
    completed = BooleanField(default=False, required=True)
    created_at = DateTimeField(default=datetime.utcnow)
    parent = StringField(required=True)

    meta = {
        "indexes": ["title"],
        "ordering": ["created_at"],
    }