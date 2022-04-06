from odoo import http, fields, models
from odoo.http import request
import json

class BajuController(http.Controller):
    @http.route(['/baju', '/baju/<int:id>'], auth='public', methods=['GET'], csrf=True)
    def getBaju(self, id=None, **kwargs):
        value = []
        if not id:
            baju = request.env['vellas.baju'].search([])
            for x in baju:
                value.append({
                    "id"            : x.id,
                    "kode_baju"     : x.kode_baju,
                    "nama_baju"     : x.name,
                    "tipe_baju"     : x.tipe_baju,
                    "ukuran_baju"   : x.ukuran_baju,
                    "jenis_bahan"   : x.jenis_bahan,
                    "harga"         : x.harga,
                    "stok"          : x.stok,
                    "keterangan"    : x.keterangan,
                })
            return json.dumps(value)
        else:
            bajuid = request.env['vellas.baju'].search([
                ('id', '=', id)
            ])
            for x in bajuid:
                value.append({
                    "id"            : x.id,
                    "kode_baju"     : x.kode_baju,
                    "nama_baju"     : x.name,
                    "tipe_baju"     : x.tipe_baju,
                    "ukuran_baju"   : x.ukuran_baju,
                    "jenis_bahan"   : x.jenis_bahan,
                    "harga"         : x.harga,
                    "stok"          : x.stok,
                    "keterangan"    : x.keterangan,
                })
            return json.dumps(value)
    
    @http.route('/baju', auth='user', type='json', methods=['POST'])
    def createBaju(self, **kw):
        if request.jsonrequest:
            if kw['nama_baju']:
                vals = {
                    "kode_baju"     : kw['kode_baju'],
                    "name"          : kw['nama_baju'],
                    "tipe_baju"     : kw['tipe_baju'],
                    "ukuran_baju"   : kw['ukuran_baju'],
                    "jenis_bahan"   : kw['jenis_bahan'],
                    "harga"         : kw['harga'],
                    "stok"          : kw['stok'],
                    "keterangan"    : kw['keterangan'],
                }
                bajuNew = request.env['vellas.baju'].create(vals)
                args = {
                    'success'       : True,
                    'ID'            : bajuNew.id
                }
                return args