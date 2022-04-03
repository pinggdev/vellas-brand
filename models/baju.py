from odoo import api, fields, models


class Baju(models.Model):
    _name = 'vellas.baju'
    _description = 'Data Baju'

    kode_baju = fields.Char(string='Kode Baju')
    name = fields.Char(string='Nama Baju')
    tipe_baju = fields.Selection([
        ('lengan_pendek', 'Lengan Pendek'),
        ('lengan_panjang', 'Lengan Panjang')
    ], string='Tipe Baju')
    ukuran_baju = fields.Selection([
        ('s', 'S'),
        ('m', 'M'),
        ('l', 'L'),
        ('xl', 'XL'),
        ('xxl', 'XXL'),
        ('xxxl', 'XXXL'),
    ], string='Ukuran Baju')
    jenis_bahan = fields.Char(string='Jenis Bahan')
    harga = fields.Integer(string='Harga')
    stok = fields.Integer(string='Stok')
    keterangan = fields.Char(string='Keterangan')