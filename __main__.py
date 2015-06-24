'''
Created on 16-01-2015

@author: mateusz
'''

# initialize_dependency_injection must be imported first in the main module to initialize all needed dependencies
import src.ioc.initialize_dependency_injection  # @UnusedImport

from src.mvc.model.offer_params import OfferParams
from src.mvc.main import Main
from src.mvc.view.desktop_main_view import DesktopMainView

# DESKTOP RUN

if __name__ == '__main__':
    city = "Krakow"
    params = OfferParams.from_key_values(city=city)
    view = DesktopMainView()
    Main.run(params, view)
