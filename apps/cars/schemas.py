from marshmallow import Schema
from marshmallow.fields import Str, Float
from apps.messages import MSG_FIELD_REQUIRED

class CarSchema(Schema):
    name = Str(required=True, error_messages={'required': MSG_FIELD_REQUIRED})
    model = Str(required=True, error_messages={'required': MSG_FIELD_REQUIRED})
    brand = Str(required=True, error_messages={'required': MSG_FIELD_REQUIRED})
    price = Float()