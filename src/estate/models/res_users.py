from odoo import models, fields



class ResUsers(models.Model):
    _name="res.users"
    _inherit="res.users"

    property_ids=fields.One2many("estate.property", "salesperson",domain=[('state','in',('new','offer_accepted','offer_received'))])
