# -*- coding: utf-8 -*-
{
    'name': "Anuwsys Webdemo",

    'summary': """Conexion con sistema webdemo de anuwsys2""",

    'description': """
        Conectamos con anuwsys2 para
            - SOLICITAR DEMOS
            - VISUALIZAR DEMOS
            - SOLICITAR WEBSITE
    """,

    'author': "Publicity with IT, S.L.",
    'website': "http://www.publiit.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],
    

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
        'views/webdemo.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
        
    ],
}