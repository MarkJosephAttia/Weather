# -*- coding: utf-8 -*-
{
    'name': "Weather",

    'summary': """Views The Weather of Cities""",

    'description': """
        Weather Project Is A Simple Project To:
            - Get The Weather Of A City
            - Adds It To A Database
            - Show Them In A Table View
            - Secure Access
    """,

    'author': "Mark Attia",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/weather_view.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}
