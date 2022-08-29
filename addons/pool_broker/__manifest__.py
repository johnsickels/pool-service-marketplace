# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Pool Broker',
    'version': '0.0',
    'category': 'Sales/Sales',
    'summary': 'Trade Pools with other Pool Service Providers',
    'description': """
This module contains the admin, customer, and user facing website for the Pool Broker.
    """,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/service_provider_views.xml',
        'views/pool_views.xml',
        'views/menus.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'assets': {
    },
    'license': 'LGPL-3',
}
