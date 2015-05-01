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
       
    def show_offers_and_params(self, offers, params):
        points = OffersGroupedByAddress.from_offers(offers).get_json_string()
        longitude, lattitude = Geocoder.geocode("%s, Polska" % params.get_city())
        
        FIELDS = {u"$POINTS$": points,
                  u"$MAP_CENTER_LONG$": longitude,
                  u"$MAP_CENTER_LATT$": lattitude,
                  u"$MAP_ZOOM$" : DesktopMainView.MAP_ZOOM}
                   
        desktop_template = DesktopMainView.config.get("PATHS", "desktopMainView")
        LightWebFramework.render_page_as_file(desktop_template, "DwellingMap.html", FIELDS)  