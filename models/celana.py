from odoo import api, fields, models


class Celana(models.Model):
    _name = 'vellas.celana'
    _description = 'Data Celana'

    kode_celana = fields.Char(string='Kode Celana')
    name = fields.Char(string='Nama Celana')
    tipe_celana = fields.Selection([
        ('celana_pendek', 'Celana Pendek'),
        ('celana_panjang', 'Celana Panjang')
    ], string='Tipe Celana')
    ukuran_celana = fields.Integer(string='Ukuran Celana')
    jenis_bahan = fields.Char(string='Jenis Bahan')
    harga = fields.Integer(string='Harga')
    stok = fields.Integer(string='Stok')
    keterangan = fields.Char(string='Keterangan')
