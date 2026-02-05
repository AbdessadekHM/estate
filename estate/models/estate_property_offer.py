from odoo import models, fields, api



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

    validity=fields.Integer(default=7, string="Validity")
    date_deadline=fields.Date(compute="_calculate_date_deadline", inverse="_inverse_deadline")

    @api.depends("validity", "create_date")
    def _calculate_date_deadline(self):
        print("calculate deadline")
        for record in self:
            record.date_deadline = fields.Datetime.add(record.create_date,days=record.validity)



    def _inverse_deadline(self):

        print("check_validity")
        for record in self:
            if record.date_deadline:
                record.validity = (fields.Date.to_date(record.date_deadline) - fields.Date.to_date(record.create_date)).days 



            
    

