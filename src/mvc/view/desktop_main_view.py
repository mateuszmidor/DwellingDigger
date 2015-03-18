'''
Created on 14-02-2015

@author: mateusz
'''
from src.mvc.view.google_map_points import GoogleMapPoints
from src.mvc.view.lightwebframework.light_web_framework import LightWebFramework
from src.outerspaceaccess.geocoder import Geocoder
from src.ioc.dependency_injector import DependencyInjector, Inject

# this zoom should be correct for most of polish major cities like Krakow and Wroclaw
MAP_ZOOM = 11

@DependencyInjector("config")
class DesktopMainView(object):

    config = Inject
    
    
    def __init__(self, city):
        "city - city in Poland to center the map on"
        self.__city = city
        
        
    def show_offers(self, offers):
        points = GoogleMapPoints.from_offers(offers).as_java_script()
        longitude, lattitude = Geocoder.geocode("%s, Polska" % self.__city)
        
        FIELDS = {u"$POINTS$": points,
                  u"$MAP_CENTER_LONG$": longitude,
                  u"$MAP_CENTER_LATT$": lattitude,
                  u"$MAP_ZOOM$" : MAP_ZOOM}
                   
        desktop_template = DesktopMainView.config.get("PATHS", "desktopMainView")
        LightWebFramework.render_page_as_file(desktop_template, "DwellingMap.html", FIELDS)  