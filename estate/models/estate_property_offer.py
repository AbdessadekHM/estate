from odoo import models, fields



class Offer(models.Model):
    _name="estate.property.offer"
    _description="offer description"

    price=fields.Float()
    status=fields.Selection([
        ('accepted', 'Accepted'),
        ('refused', 'Refused'),

    ], copy=False)

    partner_id=fields.Many2one("res.partner", string="Partner ID", required=True)
    property_id=fields.Many2one("estate.property", string="Estate Property", required=True)
    

