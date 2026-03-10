from odoo import models, fields

class Ecriture(models.Model):
    _name = 'comptabilite.ecriture'
    _description = 'Écriture Comptable'

    name = fields.Char(string='Libellé', required=True)
    compte_id = fields.Many2one('comptabilite.compte', string='Compte', required=True)
    entreprise_id = fields.Many2one('comptabilite.entreprise', string='Entreprise', required=True)
    debit = fields.Float(string='Débit')
    credit = fields.Float(string='Crédit')
    date = fields.Date(string='Date', required=True)
    numero_piece = fields.Char(string='Numéro de pièce justificative')