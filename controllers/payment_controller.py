from flask_apispec import marshal_with, doc
from flask_apispec.views import MethodResource
from flask_restful import Resource

from dtos.create_payment_response_dto import CreatePaymentResponseDto


class PaymentController(MethodResource, Resource):

    @doc(description='Api para crear un pago', tags=['Create payment'])
    @marshal_with(CreatePaymentResponseDto)
    def post(self):
        return {'result': 'False'}
