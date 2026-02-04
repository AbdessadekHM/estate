from odoo import models, fields

class Property(models.Model):
    _name = "estate.property"
    _description="easy peasy module"

    name=fields.Char(required=True)
    description=fields.Text()
    postcode=fields.Char()
    date_availability=fields.Date(copy=False, default=fields.Datetime.add(fields.Datetime.today(),months=3))
    expected_price=fields.Float(required=True)
    selling_price=fields.Float(readonly=True,copy=False)
    bedrooms=fields.Integer(default=2)
    living_area=fields.Integer()
    facades=fields.Integer()
    garage=fields.Boolean()
    garden=fields.Boolean()
    gareden_area=fields.Integer()
    garden_orientation=fields.Selection([
        ('north', 'North'),
        ('west', 'West'),
        ('east', 'East'),
        ('south', 'South')
    ], default='north')
    active=fields.Boolean()
    state=fields.Selection([
        ('new', 'New'),
        ('offer_received', 'Offer Received'),
        ('offer_accepted', 'Offer Accepted'),
        ('sold', 'Sold'),
        ('cancelled', 'Cancelled'),

    ], default='new')
    test=fields.Selection([
        ('test', 'test'),
        ('test1', 'test1'),
        ('offer_accepted', 'Offer Accepted'),
        ('sold', 'Sold'),
        ('cancelled', 'Cancelled'),

    ])

    property_type_id=fields.Many2one("estate.property.type", string="Property Type")
    salesperson=fields.Many2one("res.users", string="SalesPerson", default=lambda self: self.env.user )
    buyer=fields.Many2one("res.partner", copy=False)


    
    
    pass