'''
Created on 14-02-2015

@author: mateusz
'''
from src.mvc.model.offers_grouped_by_address import OffersGroupedByAddress
from src.mvc.view.lightwebframework.light_web_framework import LightWebFramework
from src.outerspaceaccess.geocoder import Geocoder
from src.ioc.dependency_injector import DependencyInjector, Inject


@DependencyInjector("config")
class DesktopMainView(object):

    config = Inject
    
    # this zoom should be correct for most of polish major cities like Krakow and Wroclaw
    MAP_ZOOM = 11
       
    @staticmethod
    def show_offers_and_params(offers, params):
        groups = OffersGroupedByAddress.as_json(offers)
        lattitude, longitude = Geocoder.geocode("%s, Polska" % params.get_city())
        
        fields = {u"$JSON_OFFER_GROUPS$": groups,
                  u"$MAP_CENTER_LONG$": longitude,
                  u"$MAP_CENTER_LAT$": lattitude,
                  u"$MAP_ZOOM$" : DesktopMainView.MAP_ZOOM}
                   
        desktop_template = DesktopMainView.config.get("PATHS", "desktopMainView")
        LightWebFramework.render_page_as_file(desktop_template, "DwellingMap.html", fields)  
        