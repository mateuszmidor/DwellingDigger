#!/usr/bin/python


'''
Created on 16-01-2015
This is the index file, main entry point for the web application.
@author: mateusz
'''

# initialize_dependency_injection must be imported first in the main module to initialize all needed dependencies
import src.ioc.initialize_dependency_injection  # @UnusedImport

import cgi
from src.mvc.main import Main
from src.mvc.view.web_main_view import WebMainView
from src.mvc.model.offer_params import OfferParams
from src.ioc.dependency_injector import DependencyInjector, Inject

@DependencyInjector('logger')
class Runner(object):

    logger = Inject

    @staticmethod
    def doGet():
        try:
            storage = cgi.FieldStorage()
            params = OfferParams.from_cgi_fieldstorage(storage, default_city=u"Krakow")
            view = WebMainView()
            Main.run(params, view)
        except Exception as e:
            Runner.logger.exception(e)


Runner.doGet()