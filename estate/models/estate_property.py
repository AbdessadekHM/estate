from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError #type:ignore
from odoo.tools.float_utils import float_compare, float_is_zero #type:ignore

class Property(models.Model):
    _name = "estate.property"
    _description="easy peasy module"
    _order="id desc"


    # _check_price = models.Constraint(
    #     'CHECK(expected_price>0)',
    #     'The expected price should be positive'
    # )

    # _check_selling_price = models.Constraint(
    #     'CHECK(selling_price>0) ',
    #     'The selling price should be positive'
    # )
    


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
    active=fields.Boolean(default=True)
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
    offer_ids=fields.One2many("estate.property.offer", "property_id", string="Offers")
    total_area=fields.Integer(compute="_calculate_total_area", string="Total Area", store=True)
    best_price=fields.Float(compute="_calculate_best_price", string="Best Price")



    @api.depends("garden_area","living_area")
    def _calculate_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area
    
    def _calculate_best_price(self):

        for record in self:
            if len(record.mapped("offer_ids")) == 0:
                record.best_price = 0
                continue

            record.best_price = max(record.mapped("offer_ids.price"))

        pass

    @api.onchange("garden")
    def _onchange_garden(self):
        if self.garden:
            self.garden_area=10
            self.garden_orientation="north"
        else:
            
            self.garden_area=0
            self.garden_orientation=False

        pass


    def action_do_something(self):
        print("event triggered!!")
        return True
    def sold_action(self):
        for record in self:
            if record.state =='cancelled':
                raise UserError("You can't sold a cancelled property") 
            else:
                record.state='sold'

        pass
    def cancel_action(self):

        for record in self:
            if record.state =='sold':
                raise UserError("You can't cancel a sold property") 
            else:
                record.state='cancelled'
        pass


    
    @api.constrains("selling_price")
    def _check_selling_price(self):

        for record in self:

            # # if record.selling_price < (0.9 * record.expected_price):


            price_precision = self.env['decimal.precision'].precision_get('Product Price')
            if float_compare(record.selling_price, 0.9*record.expected_price, precision_digits=price_precision) == -1  :
                raise ValidationError(f"The selling price can't be less than 90%  of ") 
            
            pass

        pass

    @api.constrains("offer_ids", "selling_price")
    def _check_offer_status(self):

        for record in self:
            status = set(record.offer_ids.mapped("status"))
            if 'accepted' not in status and record.selling_price!=0:
                raise ValidationError("Selling price won't be updated until an offer is accepted")
                
                pass



        pass



    
    
    pass