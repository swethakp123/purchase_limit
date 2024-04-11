# -*- coding: utf-8 -*-
{
    'name': "Purchase Limit",
    'version': '17.0.1.0.0',
    'depends': ['contacts','point_of_sale'],
    'category': '',
    'description': """
    Purchase limit for the customer
    """,
    'data': [
            'views/customer_form_views.xml'
             ],
    'assets': {
        'point_of_sale._assets_pos': [
            'purchase_limit/static/src/xml/partner_list_screen.xml',
            'purchase_limit/static/src/js/purchase_limit.js',
            'purchase_limit/static/src/js/partner_details.js',
        ],
    },
    'application': 'True',
    'installable': True,
}