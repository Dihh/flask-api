"""Schemas module
"""
from marshmallow import Schema, fields

class TodoSchema(Schema):
    """Todo schema
    This schema should validade todos fields and serialize response as 
    {
      "id": 0,
      "title": "string"
    }
    """
    id = fields.Int()
    title = fields.String()


class UserSchema(Schema):
    """User schema
    This schema should validade users fields and serialize response as 
    {
      "id": 0,
      "user": "string"
      "password": "string"
    }
    """
    id = fields.Int(dump_only=True)
    user = fields.String(required=True)
    password = fields.String(required=True, load_only=True)
