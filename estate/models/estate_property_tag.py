from odoo import fields,models

class Tag(models.Model):
    _name="estate.property.tag"
    _description="tag description"
    _order="name"

    _check_name=models.Constraint(
        'unique (name)',
        'Name should be unique'
    )

    name=fields.Char(required=True)
    color=fields.Integer(string="Color")
    