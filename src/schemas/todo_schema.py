"""Todo schema module
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
