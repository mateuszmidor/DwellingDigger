'''
Created on 16-01-2015

@author: mateusz
'''
from src.mvc.model.offer_params import OfferParams
from src.mvc.main import Main
from src.mvc.view.desktop_main_view import DesktopMainView

'''
DEMO RUN
'''
if __name__ == '__main__':
    #Controller.demo_run()
    params = OfferParams.from_key_values(city="Krakow", min_price=2999)
    Main.run(params, DesktopMainView())