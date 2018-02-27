# -*- coding: utf-8 -*-
{
    'name': "QL_DeTai",

    'summary': """Manage trainings""",

    'description': """
    """,

    'author': "Phat",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hr'
    ],

    # always loaded
    'data': [
        'View.xml'
        # 'security/ir.model.access.csv',

    ],
    # only loaded in demonstration mode
    'demo': [
        'View.xml'
    ],
}