from odoo import api, fields, models


class Partner(models.Model):
    _inherit = 'res.partner'

    vellas_pegawai = fields.Boolean(string='Pegawai', default=False)
    vellas_pelanggan = fields.Boolean(string='Pelanggan', default=False)
    
    