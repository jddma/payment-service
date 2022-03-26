from marshmallow import Schema
from marshmallow import fields


class CreatePaymentResponseDto(Schema):
    result = fields.Str(default='ex')
