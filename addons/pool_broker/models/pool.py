# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class Pool(models.Model):
    _name = 'pool_broker.pool'
    _description = 'A home with a pool, ready to be traded or recently traded'
    _rec_name = "location"

    location = fields.Many2one('res.city', required=True)
    monthly_price = fields.Float()
    current_service_provider = fields.Many2one('pool_broker.service_provider')
