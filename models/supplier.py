from odoo import api, fields, models


class Supplier(models.Model):
    _name = 'vellas.supplier'
    _description = 'Data Supplier'

    name = fields.Char(string='Nama Penyedia Supplier')
    barang_supplier = fields.Char(string='Barang Supplier')
    telpon = fields.Char(string='Nomor Telepon')
    alamat = fields.Char(string='Alamat')
    
    
