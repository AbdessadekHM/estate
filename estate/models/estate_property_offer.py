from odoo import models, fields, api
from odoo.exceptions import UserError #type:ignore



class Offer(models.Model):
    _name="estate.property.offer"
    _description="offer description"
    _check_price = models.Constraint(
        'CHECK(price>0)',
        'The offer price should be positive'
    )

    price=fields.Float()
    status=fields.Selection([
        ('accepted', 'Accepted'),
        ('refused', 'Refused'),

    ], copy=False)

    partner_id=fields.Many2one("res.partner", string="Partner ID", required=True)
    # partner_id=fields.Many2one("res.partner", string="Partner ID")
    property_id=fields.Many2one("estate.property", string="Estate Property", required=True)

    validity=fields.Integer(default=7, string="Validity")
    date_deadline=fields.Date(compute="_calculate_date_deadline", inverse="_inverse_deadline")

    @api.depends("validity", "create_date")
    def _calculate_date_deadline(self):
        print("calculate deadline")
        for record in self:
            if record and record.create_date:
                record.date_deadline = fields.Datetime.add(record.create_date,days=record.validity)
            pass



    def _inverse_deadline(self):

        print("check_validity")
        for record in self:
            if record.date_deadline:
                record.validity = (fields.Date.to_date(record.date_deadline) - fields.Date.to_date(record.create_date)).days 

    def action_confirm(self):
        for record in self:
            if record.status == 'refused':
                raise UserError("can't accept a refused offer")
            # elif record.status=='accepted':
            #     raise UserError("Offer already accepted")
            else:
                record.status=='accepted'
                record.property_id.selling_price=record.price
                record.property_id.buyer=record.partner_id
        return True
    
    def action_cancel(self):
        for record in self:
            
            if record.status == 'accepted':
                raise UserError("can't accept an accepeted offer")
            # elif record.status=='refused':
            #     raise UserError("Offer already refused")
            else:
                record.status=='refused'
        return True



            
    

