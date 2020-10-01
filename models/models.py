# -*- coding: utf-8 -*-

from odoo import models, fields, api
import urllib
import json

class weather(models.Model):
    _name = 'weather.weather'
    _description = 'The Weather Model'
    city = fields.Text(string='city', required=True)
    weather = fields.Text(string='weather', required=False)
    temperature = fields.Text(string='temperature', required=False)