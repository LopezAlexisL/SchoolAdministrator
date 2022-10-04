from odoo import api, fields, models


class School(models.Model):
    _name = 'school.lines'
    _description = 'Teacher shedule organizator'

    school_name = fields.Char(string='School Name')
    school_code = fields.Char(string='School Code')
    address = fields.Char(string='Address')
    location = fields.Char(string='Location')
    hours = fields.Integer(string='Internal Hours')
    school_type = fields.Selection(selection=[('adult', 'Adult'),('highschool', 'Highschool')], string='Type of school')
    job_type = fields.Selection(selection=[('tutor', 'Tutor'), ('teacher', 'Teacher')])
    course = fields.Char(string='Courses')
    hours_ids = fields.One2many(comodel_name='hours.lines', inverse_name='school_id')
    asignature = fields.Char(string='Asignature')