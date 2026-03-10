from odoo import models, fields

class Entreprise(models.Model):
    _name = 'comptabilite.entreprise'
    _description = 'Entreprise gérée par le cabinet'

    name = fields.Char(string='Nom de l’entreprise', required=True)
    nif = fields.Char(string='NIF', required=True)
    secteur = fields.Char(string='Secteur d’activité')