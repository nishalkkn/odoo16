# -*- coding: utf-8 -*-
from odoo import fields, models


class StockReportWizard(models.TransientModel):
    _name = 'stock.report.wizard'
    _description = "Stock Report Wizard"

    from_date = fields.Date('From Date', help="Report shown from which date")
    to_date = fields.Date('End Date', help="Report shown upto which date")
    usage = fields.Selection([
        ('supplier', 'Vendor Location'),
        ('view', 'View'),
        ('internal', 'Internal Location'),
        ('customer', 'Customer Location'),
        ('inventory', 'Inventory Loss'),
        ('production', 'Production'),
        ('transit', 'Transit Location')], 'Location Type', help="Report shown for which location type")
    product_id = fields.Many2one('product.template', 'Product', help="Report shown for which product")
    status = fields.Char()

    def action_print_pdf(self):
        """print pdf button in wizard"""
        data = {
            'from_date': self.from_date,
            'to_date': self.to_date,
            'usage': self.usage,
            'product_id': self.product_id.id,
            'status': self.status
        }
        return self.env.ref('stock_advanced_move_report.action_report_stock').report_action(None, data=data)




    # def action_print_exel(self):
    #     """print exel button in wizard"""
    #     data = {
    #         'machine_id': self.machine_id.id,
    #         'from_date': self.from_date,
    #         'to_date': self.to_date,
    #         'customer_id': self.customer_id.id,
    #         'transfer_type': self.transfer_type
    #     }
    #     return {
    #         'type': 'ir.actions.report',
    #         'data': {
    #             'model': 'report.machine_management.machine_transfer_report',
    #             'options': json.dumps(data, default=date_utils.json_default),
    #             'output_format': 'xlsx',
    #             'report_name': 'Machine Transfer Excel Report',
    #         },
    #         'report_type': 'xlsx',
    #     }
