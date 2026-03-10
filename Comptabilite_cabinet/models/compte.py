from odoo import models, fields

class Compte(models.Model):
    _name = 'comptabilite.compte'
    _description = 'Compte Comptable'

    name = fields.Char(string='Nom du compte', required=True)
    code = fields.Char(string='Code du compte', required=True)
    entreprise_id = fields.Many2one('comptabilite.entreprise', string='Entreprise', required=True)