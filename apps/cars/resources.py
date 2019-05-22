from flask_restful import Resource

from .models import Car
from .schemas import CarSchema

from apps.messages import MSG_EXCEPTION, MSG_RESOURCE_FETCHED
from apps.responses import resp_exception, resp_ok

class CarResource(Resource):
    def get(self):
        schema = CarSchema(many=True)

        try:
            cars = Car.objects()
            
            result = schema.dump(cars)
            
            return resp_ok('Car', MSG_RESOURCE_FETCHED.format('Cars'), data=result.data)
        except Exception as e:
            return resp_exception('Car', description=e.__str__())

