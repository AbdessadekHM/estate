from odoo import models, fields

class PropertyType(models.Model):
    _name="estate.property.type"
    _description="a model describe the property type"
    _check_name=models.Constraint(
        'unique (name)',
        'Each name must be unique'
    )

    name=fields.Char(required=True)
    # description=fields.Char()



