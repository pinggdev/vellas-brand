from odoo import api, fields, models


class Penjualan(models.Model):
    _name = 'vellas.penjualan'
    _description = 'New Description'

    penjualandetail_ids = fields.One2many(comodel_name='vellas.penjualandetail', inverse_name='penjualan_id', string='Penjualan Detail')

    name = fields.Char(string='Kode Penjualan')
    tanggal = fields.Datetime(string='Tanggal', default=fields.Datetime.now())
    pelanggan_id = fields.Many2one(comodel_name='res.partner', string='Pelanggan', domain=[('vellas_pelanggan', '=', True)])
    total = fields.Integer(compute='_compute_total', string='Total', store=True)
    
    @api.depends('penjualandetail_ids')
    def _compute_total(self):   
        for record in self:
            a = sum(self.env['vellas.penjualandetail'].search([('penjualan_id', '=', record.id)]).mapped('harga_total'))
            record.total = a


class PenjualanDetail(models.Model):
    _name = 'vellas.penjualandetail'
    _description = 'New Description'

    penjualan_id = fields.Many2one(comodel_name='vellas.penjualan', string='Penjualan')
    produk_id = fields.Many2one(comodel_name='vellas.produk', string='Produk')

    name = fields.Char(string='Name')
    qty = fields.Integer(string='Kuantitas')
    harga_satuan = fields.Integer(compute='_compute_harga_satuan', string='Harga Satuan')
    harga_total = fields.Integer(compute='_compute_harga_total', string='Harga Total')
    
    @api.depends('qty', 'harga_satuan')
    def _compute_harga_total(self):
        for record in self:
            record.harga_total = record.harga_satuan * record.qty
    
    @api.depends('produk_id')
    def _compute_harga_satuan(self):
        for record in self:
            record.harga_satuan = record.produk_id.harga
    
    @api.model
    def create(self,vals):
        record = super(PenjualanDetail, self).create(vals) 
        if record.qty:
            self.env['vellas.produk'].search([('id','=',record.produk.id.id)]).write({'stok':record.produk_id.stok-record.qty})
            return record

    