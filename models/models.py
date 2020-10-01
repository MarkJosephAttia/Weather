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
    @api.model
    def create(self, values):
        domain = 'https://api.openweathermap.org/data/2.5/weather?q='
        appid = '&appid=3c1ae8d9da743c95fa27bf4aee329a61'
        if (values['city'] != ''):
            try:
                with urllib.request.urlopen(domain + values['city'] + appid) as url:
                    js_tmp = json.loads(url.read())
                    values['weather'] = js_tmp['weather'][0]['description']
                    values['temperature'] = js_tmp['main']['temp']
            except:
                None
        res = super(weather, self).create(values)
        return res