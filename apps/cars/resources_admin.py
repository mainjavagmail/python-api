from flask_restful import Resource
from flask import request
from flask_jwt_extended import jwt_required

from .schemas import CarSchema
from .models import Car

from apps.messages import MSG_NO_DATA, MSG_INVALID_DATA, MSG_EXCEPTION, MSG_RESOURCE_CREATED
from apps.responses import resp_data_invalid, resp_exception, resp_ok


class AdminCarResource(Resource):
    @jwt_required
    def post(self, *args, **kwargs):
        req_data = request.get_json() or None
        data, errors, result = None, None, None
        schema = CarSchema()

        if req_data is None:
            return resp_data_invalid('Car', [], MSG_NO_DATA)

        data, errors = schema.load(req_data)

        if errors:
            return resp_data_invalid('Car', [], MSG_INVALID_DATA)

        try:
            model = Car(**data)
            model.save()

            schema = CarSchema()
            result = schema.dump(model)

            return resp_ok('Car', MSG_RESOURCE_CREATED.format('Car'), data=result.data)
        except Exception as e:
            return resp_exception('Car', 'Exception to save car', MSG_EXCEPTION)


