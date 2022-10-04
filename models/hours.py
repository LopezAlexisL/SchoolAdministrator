from odoo import api, fields, models


class HoursLines(models.Model):
    _name = 'hours.lines'

    day = fields.Selection(selection=[('mon', '1-Monday'), ('tue', '2-Tuesday'), ('wed', '3-Wednesday'), ('thu', '4-Thursday'), ('fri', '5-Friday')], string='Days')
    shift = fields.Selection(selection=[('mor', '1-Morning'), ('aft', '2-Afternoon'), ('nig', '3-Night')], string='Shift')
    from_hs = fields.Float(string='From')
    to_hs = fields.Float(string='To')
    school_id = fields.Many2one(comodel_name='school.lines', invisible=True)