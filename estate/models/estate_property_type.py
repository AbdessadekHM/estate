from odoo import models, fields

class PropertyType(models.Model):
    _name="estate.property.type"
    _description="a model describe the property type"
    _order="sequence,name"
    _check_name=models.Constraint(
        'unique (name)',
        'Each name must be unique'
    )

    name=fields.Char(required=True)
    sequence=fields.Integer('Sequence', default=1,help="Used to order types")
    property_ids=fields.One2many("estate.property","property_type_id", string="Property ID")

    # description=fields.Char()



