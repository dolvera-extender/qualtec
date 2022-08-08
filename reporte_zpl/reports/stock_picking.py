# -*- coding: utf-8 -*-

from odoo import fields, models
import logging
_logger = logging.getLogger(__name__)


class StockPicking(models.Model):
    _name = "zpl.report"
    _inherit = "stock.picking"
    
    def send_zpl_report(self):
        _logger.info("si se ejecutaaaa")
        _logger.info(self)
        _logger.info("si se ejecutaaaa")
        
