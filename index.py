#!/usr/bin/python
'''
Created on 16-01-2015

This is the index file, main entry point for the web application.

@author: mateusz
'''

import cgi
from src.mvc.main import Main
from src.mvc.view.web_main_view import WebMainView
from src.mvc.model.offer_params import OfferParams


storage = cgi.FieldStorage()
params = OfferParams.from_cgi_fieldstorage(storage)
Main.run(params, WebMainView())