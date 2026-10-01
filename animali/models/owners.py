from odoo import models, fields

class Owners(models.Model):
    _name = "gestione.owners"
    _description = "Owners"
    name = fields.Char(string="Nome e Cognome")
    eta = fields.Ineger(string="Eta'")
    animal_ids = fields.One2many("gestione.animals", "owner_id", string="Animali")