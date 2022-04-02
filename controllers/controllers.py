# -*- coding: utf-8 -*-
# from odoo import http


# class VellasBrand(http.Controller):
#     @http.route('/vellas_brand/vellas_brand/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vellas_brand/vellas_brand/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vellas_brand.listing', {
#             'root': '/vellas_brand/vellas_brand',
#             'objects': http.request.env['vellas_brand.vellas_brand'].search([]),
#         })

#     @http.route('/vellas_brand/vellas_brand/objects/<model("vellas_brand.vellas_brand"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vellas_brand.object', {
#             'object': obj
#         })
