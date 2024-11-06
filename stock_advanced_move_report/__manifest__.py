# -*- coding: utf-8 -*-
{
    'name': "Stock Advanced Move Report",
    'application': True,
    'version': '16.0.1.0.1',
    'summary': 'showing the advanced move report of the stock',
    'description': """
This module allows to view the advanced stock move report of the stock.
    """,

    'depends': [
        'base',
        'stock',
    ],

    'data': [
        'security/ir.model.access.csv',

        'wizard/stock_report_wizard.xml',
        'report/ir_actions_report.xml',
        'report/stock_report.xml',
    ],

    'license': 'LGPL-3',

}
