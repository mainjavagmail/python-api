from apps.db import db

from mongoengine import (
    StringField,
    FloatField
)

class Car(db.Document):
    name = StringField(required=True, max_length=60)
    model = StringField(required=True, max_length=30)
    brand = StringField(required=True, max_length=60)
    price = FloatField(default=0.0)
