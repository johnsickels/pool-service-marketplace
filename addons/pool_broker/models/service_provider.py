# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, _


class ServiceProvider(models.Model):
    _name = 'pool_broker.service_provider'
    _description = 'A pool cleaning business, actively trading pools on their route.'
    # _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char()
    state = fields.Selection([
        ('unqualified', 'Unqualified'),
        ('not_interested', 'Not Interested'),
        ('needs_follow_up', 'Needs Follow-Up'),
        ('interested', 'Interested'),
    ], string='Status')
    date_contacted = fields.Date()
    phone = fields.Char()
    desired_locations = fields.Many2many('res.city')
    contact = fields.Char()
    contact_position = fields.Char()
    notes = fields.Text()

    pools_to_trade = fields.One2many(
        'pool_broker.pool', 'current_service_provider')
