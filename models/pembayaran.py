from odoo import api, fields, models


class Pembayaran(models.Model):
    _name = 'vellas.pembayaran'
    _description = 'Pembayaran Produk Vellas'

    penjualan_id = fields.Many2one(comodel_name='vellas.penjualan', string='Penjualan')

    name = fields.Char(compute='_compute_nama_pembeli', string='Nama Pembeli')
    
    @api.depends('penjualan_id')
    def _compute_nama_pembeli(self):
        for record in self:
            record.name = self.env['vellas.penjualan'].search([('id', '=', record.penjualan_id.id)]).mapped('pelanggan_id').name

    tanggal_bayar = fields.Date(string='Tanggal Bayar', default=fields.Date.today())
    total = fields.Integer(compute='_compute_total', string='Total')
    
    @api.depends('penjualan_id')
    def _compute_total(self):
        for record in self:
            record.total = record.penjualan_id.total

    metode_bayar = fields.Selection([
        ('tunai', 'Tunai'),
        ('transfer', 'Transfer'),
    ], string='Metode Bayar')

    @api.model
    def create(self,vals):
        record = super(Pembayaran, self).create(vals) 
        if record.tanggal_bayar:
            self.env['vellas.penjualan'].search([('id','=',record.penjualan_id.id)]).write({'sudah_bayar':True})
            return record
    
