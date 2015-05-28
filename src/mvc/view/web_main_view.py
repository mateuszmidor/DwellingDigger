'''
Created on 04-03-2015

@author: mateusz
'''
from src.mvc.view.lightwebframework.light_web_framework import LightWebFramework
from src.ioc.dependency_injector import DependencyInjector, Inject
from src.outerspaceaccess.geocoder import Geocoder
from src.mvc.view.lightwebframework.user_agent import UserAgent
from src.mvc.model.offers_grouped_by_address import OffersGroupedByAddress


@DependencyInjector("config")
class WebMainView(object):

    config = Inject
        
    def show_offers_and_params(self, offers, params):
        ''' Show offers on the map, fill the search form fields with previously used params '''
        if UserAgent.is_mobile():
            self.show_mobile(offers, params)
        else:
            self.show_desktop(offers, params)
        
        
    def show_mobile(self, offers, params):
        ''' For mobile devices '''
        MAP_ZOOM = 11
        fields = self.get_fields(offers, params, MAP_ZOOM)
        web_page__template = WebMainView.config.get("PATHS", "m.webMainView")                   
        LightWebFramework.render_page_as_http_response(web_page__template, fields)        
        
        
    def show_desktop(self, offers, params):
        ''' For desktop devices '''
        MAP_ZOOM = 12
        fields = self.get_fields(offers, params, MAP_ZOOM)
        web_page__template = WebMainView.config.get("PATHS", "webMainView")                   
        LightWebFramework.render_page_as_http_response(web_page__template, fields)      
        
        
    def get_fields(self, offers, params, zoom): 
        groups = OffersGroupedByAddress.as_json(offers)
        lattitude, longitude = Geocoder.geocode("%s, Polska" % params.get_city())
        num_rooms = params.get_num_rooms() or u""
        max_price = params.get_max_price() or u""
        whereabouts = params.get_whereabouts() or u""
                 
        FIELDS = {u"$JSON_OFFER_GROUPS$": groups,
                  u"$MAP_CENTER_LONG$": longitude,
                  u"$MAP_CENTER_LAT$": lattitude,
                  u"$MAP_ZOOM$" : zoom,
                  u"$NUM_ROOMS$" : num_rooms,
                  u"$MAX_PRICE$" : max_price,
                  u"$WHEREABOUTS$" : whereabouts}   
        return FIELDS      