from flask_marshmallow.fields import fields
from marshmallow import validates
from flask_marshmallow.schema import Schema
from app.modules.core import utils


class CreateUserSchema(Schema):
    fullname = fields.Str(required=True)
    password = fields.Str(required=True)
    email = fields.Str(required=True)
    cpf = fields.Str(required=True)

    @validates("fullname")
    def validate_fullname(self, value):
        utils.valid_name(value)

    @validates("password")
    def validate_password(self, value):
        utils.valid_password(value)

    @validates("email")
    def validate_email(self, value):
        utils.valid_email(value)

    @validates("cpf")
    def validate_cpf(self, value):
        utils.valid_cpf(value)
