from odoo import api, fields, models


class Produk(models.Model):
    _name = 'vellas.produk'
    _description = 'Data Produk'

    kode_produk = fields.Char(string='Kode Produk')
    name = fields.Char(string='Nama Produk')
    harga = fields.Integer(string='Harga')
    stok = fields.Integer(string='Stok')
    satuan = fields.Selection([
        ('kg', 'Kg'),
        ('pcs', 'Pcs'),
        ('lusin', 'Lusin')
    ], string='Satuan')
    supplier_id = fields.Many2one(comodel_name='vellas.supplier', string='Supplier')
    
    
    
    
    