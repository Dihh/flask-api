"""auth schema module
"""
from marshmallow import Schema, fields

class SystemAuthSchema(Schema):
    """ErrorSchema schema
    This schema should serialize auth response as 
    {
        "access_token": "string"
    }
    """
    access_token = fields.String()
