from odoo import models, fields, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order'

    from_datetime = fields.Datetime("From")
    to_datetime = fields.Datetime("To")

    def create_calendar_events(self):
        for record in self:
            if record.from_datetime < record.to_datetime:
                for line in record.order_line:
                    self.env['calendar.event'].create({
                        'name': line.product_id.name,
                        'start': record.from_datetime,
                        'stop': record.to_datetime,
                        'product_id': line.product_id.id,
                        'partner_ids': [
                            (4, self.env.user.partner_id.id),
                            (4, record.partner_id.id),
                        ],
                    })
        return self.env.ref('calendar.action_calendar_event').read()[0]


class CalendarEvent(models.Model):
    _inherit = 'calendar.event'

    product_id = fields.Many2one('product.product', string="Product")


