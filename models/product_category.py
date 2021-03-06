# -*- coding: utf-8 -*-

from odoo import api, fields, tools, models
import logging

_logger = logging.getLogger(__name__)


class ProductCategory(models.Model):
    _inherit = "product.category"

    enable_indexation_raw_material = fields.Boolean(string="Enable indexation raw material",
                                                    help="Only for normal product.category, "
                                                         "enable indexation raw material.")
    indexation_raw_material_lines_ids = fields.One2many(comodel_name="indexation.raw_material.lines",
                                                        inverse_name="category_id",
                                                        domain=[('field_enable', '=', True)])
    average_indexation = fields.Float(compute='average_indexation_raw_materials_ids', digits=(16, 6))

    @api.depends('indexation_raw_material_lines_ids')
    def average_indexation_raw_materials_ids(self):
        for record in self:
            if not record.enable_indexation_raw_material:
                continue

            # Sum all indexation if active
            sum_indexation = 0.
            max_product_qty = 0.

            for indexation_line in record.indexation_raw_material_lines_ids:
                if not indexation_line.field_enable:
                    continue
                # Apply indexation with product qty
                sum_indexation += indexation_line.indexation_value * indexation_line.product_qty
                max_product_qty += indexation_line.product_qty

            # Fill value, protect from divide by zero
            if max_product_qty:
                record.average_indexation = sum_indexation / max_product_qty
            else:
                record.average_indexation = 0.

    @api.multi
    def apply_indexation_raw_material_on_product_category(self, cxt):
        for record in self.browse(cxt['active_ids']):
            self.env['indexation.raw_material'].apply_indexation(category_id=record)
