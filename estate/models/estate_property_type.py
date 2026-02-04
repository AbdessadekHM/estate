from odoo import models, fields

class PropertyType(models.Model):
    _name="estate.property.type"
    _description="a model describe the property type"

    name=fields.Char(required=True)
    # description=fields.Char()



