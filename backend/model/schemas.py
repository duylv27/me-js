from marshmallow import Schema, fields

class ItemSchema(Schema):
    id = fields.Int(dump_only=True)  # Read-only field, only included in responses
    content = fields.Str(required=True)
    priority = fields.Int(required=True)
    created_date = fields.Date(required=True)
    created_by = fields.Str(required=True)  # Assuming `created_by` is a string (adjust if different)
    updated_date = fields.Date(required=True)

# Usage example
item_schema = ItemSchema()  # For single items
items_schema = ItemSchema(many=True)  # For lists of items