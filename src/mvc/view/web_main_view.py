'''
Created on 04-03-2015

@author: mateusz
'''
from src.mvc.view.google_map_points import GoogleMapPoints
from src.mvc.view.lightwebframework.light_web_framework import LightWebFramework
from src.ioc.dependency_injector import DependencyInjector, Inject
from src.outerspaceaccess.geocoder import Geocoder

# this zoom should be correct for most of polish major cities like Krakow and Wroclaw
MAP_ZOOM = 11

@DependencyInjector("config")
class WebMainView(object):

    config = Inject
        
    def show_offers_and_params(self, offers, params):
        points = GoogleMapPoints.from_offers(offers).as_java_script()
        longitude, lattitude = Geocoder.geocode("%s, Polska" % params.get_city())
        num_rooms = params.get_num_rooms() or u""
        max_price = params.get_max_price() or u""
        whereabouts = params.get_whereabouts() or u""
        
        FIELDS = {u"$POINTS$": points,
                  u"$MAP_CENTER_LONG$": longitude,
                  u"$MAP_CENTER_LATT$": lattitude,
                  u"$MAP_ZOOM$" : MAP_ZOOM,
                  u"$NUM_ROOMS$" : num_rooms,
                  u"$MAX_PRICE$" : max_price,
                  u"$WHEREABOUTS$" : whereabouts}
                   
        web_page__template = WebMainView.config.get("PATHS", "webMainView")                   
        LightWebFramework.render_page_as_http_response(web_page__template, FIELDS) 
        