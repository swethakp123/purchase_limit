# -*- coding: utf-8 -*-
from odoo import models, fields


class PurchaseLimit(models.Model):
    _inherit = 'res.partner'

    activate_purchase_limit = fields.Boolean(string="Active Purchase Limit", default=False)
    purchase_limit = fields.Integer(string="Purchase Limit Amount")
