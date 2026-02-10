from odoo import models, fields, Command

class EstateProperty(models.Model):
    _name="estate.property"
    _inherit="estate.property"

    def sold_action(self):


        for record in self:



            data = {
                'partner_id': record.buyer,
                'move_type': 'out_invoice', 
                'line_ids': [
                    Command.create({
                        "name":record.name,
                        "quantity": 1,
                        "price_unit": record.selling_price

                    })

                ]
            }

            self.env['account.move'].create(data)


        
        return super().sold_action()



    pass