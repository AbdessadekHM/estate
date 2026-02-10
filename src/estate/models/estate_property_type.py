from odoo import models, fields, api

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

    offer_ids=fields.One2many("estate.property.offer", "property_type_id")
    offer_count=fields.Integer(compute="_count_offers")


    @api.depends("offer_ids")
    def _count_offers(self):
        for record in self:
            record.offer_count=len(record.offer_ids)
    

    
    

    # description=fields.Char()



