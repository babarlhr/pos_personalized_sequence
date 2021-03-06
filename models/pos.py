# -*- coding: utf-8 -*-

from odoo import fields, models

class PosConfig(models.Model):
    _inherit = 'pos.config'

    personalized_sequence_id = fields.Many2one('ir.sequence', 'personalized Order IDs Sequence')


class PosOrder(models.Model):
    _inherit = 'pos.order'

    def pos_personalized_sequence(self, sequence):
        sequence = self.env['ir.sequence'].sudo().browse([sequence])
        return sequence.next_by_id()
