from odoo import api, fields, models


class Penjualan(models.Model):
    _name = 'vellas.penjualan'
    _description = 'New Description'

    penjualanbajudetail_ids = fields.One2many(comodel_name='vellas.penjualanbajudetail', inverse_name='penjualan_id', string='Penjualan Baju Detail')
    penjualancelanadetail_ids = fields.One2many(comodel_name='vellas.penjualancelanadetail', inverse_name='penjualanc_id', string='Penjualan Celana Detail')

    name = fields.Char(string='Kode Penjualan')
    tanggal = fields.Datetime(string='Tanggal', default=fields.Datetime.now())
    pelanggan_id = fields.Many2one(comodel_name='res.partner', string='Pelanggan', domain=[('vellas_pelanggan', '=', True)])
    total = fields.Integer(compute='_compute_total', string='Total', store=True)
    
    @api.depends('penjualanbajudetail_ids')
    def _compute_total(self):   
        for record in self:
            a = sum(self.env['vellas.penjualanbajudetail'].search([('penjualan_id', '=', record.id)]).mapped('harga_total'))
            b = sum(self.env['vellas.penjualancelanadetail'].search([('penjualanc_id', '=', record.id)]).mapped('harga_total'))
            record.total = a + b


class PenjualanBajuDetail(models.Model):
    _name = 'vellas.penjualanbajudetail'
    _description = 'New Description'

    penjualan_id = fields.Many2one(comodel_name='vellas.penjualan', string='Penjualan')
    baju_id = fields.Many2one(comodel_name='vellas.baju', string='Baju')

    name = fields.Char(string='Name')
    qty = fields.Integer(string='Kuantitas')
    harga_satuan = fields.Integer(compute='_compute_harga_satuan', string='Harga Satuan')
    harga_total = fields.Integer(compute='_compute_harga_total', string='Harga Total')
    
    @api.depends('qty', 'harga_satuan')
    def _compute_harga_total(self):
        for record in self:
            record.harga_total = record.harga_satuan * record.qty
    
    @api.depends('baju_id')
    def _compute_harga_satuan(self):
        for record in self:
            record.harga_satuan = record.baju_id.harga
    
    @api.model
    def create(self,vals):
        record = super(PenjualanBajuDetail, self).create(vals) 
        if record.qty:
            self.env['vellas.baju'].search([('id','=',record.baju.id.id)]).write({'stok':record.baju_id.stok-record.qty})
            return record

class PenjualanCelanaDetail(models.Model):
    _name = 'vellas.penjualancelanadetail'
    _description = 'New Description'

    penjualanc_id = fields.Many2one(comodel_name='vellas.penjualan', string='Penjualan')
    celana_id = fields.Many2one(comodel_name='vellas.celana', string='Celana')

    name = fields.Char(string='Name')
    qty = fields.Integer(string='Kuantitas')
    harga_satuan = fields.Integer(compute='_compute_harga_satuan', string='Harga Satuan')
    harga_total = fields.Integer(compute='_compute_harga_total', string='Harga Total')
    
    @api.depends('qty', 'harga_satuan')
    def _compute_harga_total(self):
        for record in self:
            record.harga_total = record.harga_satuan * record.qty
    
    @api.depends('celana_id')
    def _compute_harga_satuan(self):
        for record in self:
            record.harga_satuan = record.celana_id.harga
    
    @api.model
    def create(self,vals):
        record = super(PenjualanCelanaDetail, self).create(vals) 
        if record.qty:
            self.env['vellas.celana'].search([('id','=',record.celana.id.id)]).write({'stok':record.celana_id.stok-record.qty})
            return record


    