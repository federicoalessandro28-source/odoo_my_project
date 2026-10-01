from odoo import models, fields

class Animals(models.Model):
    _name = "gestione.animals"
    _description = "Animals"
    name = fields.Char(string="Nome Animale", required=True)
    specie = fields.Selection([("cane", "Cane") 
                               ("gatto", "Gatto")
                               ("altro", "Altro")],
                                string="Specie", default="Cane")
    
    owner_id = fields.Many2one("gestione.owners", string="Proprietario")