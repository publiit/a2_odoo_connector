# -*- coding: utf-8 -*-

from odoo import models, fields, api

class demostracion_web(models.Model):
     _name = 'a2_webdemo.demostracion'

     nombre = fields.Char()     
     uri  = fields.Char()
     
     cliente = fields.Many2one('res.partner', string="Cliente")