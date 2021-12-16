# ©️ OdooPBX by Odooist, Odoo Proprietary License v1.0, 2021
from odoo import models, fields, api, _


class Tag(models.Model):
    _name = 'asterisk_plus.tag'
    _description = 'Recording Tag'

    name = fields.Char(required=True)
    recordings = fields.Many2many('asterisk_plus.recording',
                                  relation='asterisk_plus_recording_tag',
                                  column1='recording', column2='tag')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', _('The name must be unique!')),
    ]

    @api.model
    def create(self, vals):
        res = super(Tag, self).create(vals)
        return res

