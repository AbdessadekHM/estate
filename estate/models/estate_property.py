from odoo import models, fields, api

class Property(models.Model):
    _name = "estate.property"
    _description="easy peasy module"

    name=fields.Char(required=True)
    description=fields.Text()
    postcode=fields.Char()
    date_availability=fields.Date(copy=False, default=fields.Datetime.add(fields.Datetime.today(),months=3), string="Available From")
    expected_price=fields.Float(required=True)
    selling_price=fields.Float(readonly=True,copy=False)
    bedrooms=fields.Integer(default=2, string="Bedrooms")
    living_area=fields.Integer(string="Living Area (sqm)")
    facades=fields.Integer()
    garage=fields.Boolean(string="Garage")
    garden=fields.Boolean(string="Garden")
    garden_area=fields.Integer(string="Garden Area (sqm)")
    garden_orientation=fields.Selection([
        ('north', 'North'),
        ('west', 'West'),
        ('east', 'East'),
        ('south', 'South')
    ], default='north',string="Garden Orientation")
    active=fields.Boolean()
    state=fields.Selection([
        ('new', 'New'),
        ('offer_received', 'Offer Received'),
        ('offer_accepted', 'Offer Accepted'),
        ('sold', 'Sold'),
        ('cancelled', 'Cancelled'),

    ], default='new')

    property_type_id=fields.Many2one("estate.property.type", string="Property Type")
    salesperson=fields.Many2one("res.users", string="SalesPerson", default=lambda self: self.env.user )
    buyer=fields.Many2one("res.partner", copy=False)
    tag_ids=fields.Many2many("estate.property.tag")
    offer_ids=fields.One2many("estate.property.offer", "partner_id", string="Offers")
    total_area=fields.Integer(compute="_calculate_total_area", string="Total Area")
    best_price=fields.Float(compute="_calculate_best_price", string="Best Price")



    @api.depends("garden_area","living_area")
    def _calculate_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area
    
    def _calculate_best_price(self):

        for record in self:
            if len(record.mapped("offer_ids.price")) == 0:
                record.best_price = 0
                continue

            record.best_price = max(record.mapped("offer_ids.price"))

        pass


    # def action_do_something(self):
    #     print("do something")
    #     print(self)
    #     for record in self:
    #         record.test='sold'
    #     return True


    
    
    pass