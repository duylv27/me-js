from marshmallow import Schema, fields
from sqlalchemy import Integer


class ItemSchema(Schema):
    id = fields.Int(dump_only=True)
    content = fields.Str(required=True)
    priority = fields.Int(required=True)
    created_date = fields.Date(required=True)
    created_by = fields.Str(required=True)
    updated_date = fields.Date(required=True)

item_schema = ItemSchema()
items_schema = ItemSchema(many=True)

class RoleSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True)
    roles = fields.List(fields.Int, required=True)

user_schema = UserSchema()
users_schema = UserSchema(many=True)