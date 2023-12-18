from odoo import models, fields

class MonModule(models.Model):
    _name = 'mon.module'
    _description = 'mon module test'

    name = fields.Char(string='Nom', required=True)
    description = fields.Text(string='Description')
    date_creation = fields.Date(string='Date de création', default=fields.Date.today)
