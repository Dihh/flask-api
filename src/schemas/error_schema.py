"""Todo schema module
"""
from marshmallow import Schema, fields

class ErrorMEssageSchema(Schema):
    """ErrorMEssageSchema schema
    This schema have errors fields
    """
    reason = fields.String()

class SystemErrorSchema(Schema):
    """ErrorSchema schema
    This schema should serialize errors response as 
    {
      "error": {
        "reason": "string"
      }
    }
    """
    error = fields.Nested(ErrorMEssageSchema)
