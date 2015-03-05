'''
Created on 14-02-2015

@author: mateusz
'''
from src.mvc.view.google_map_points import GoogleMapPoints
from src.mvc.view.lightwebframework.light_web_framework import LightWebFramework

MAP_CENTER_LONG = 50.0646501 
MAP_CENTER_LATT = 19.9449799
MAP_ZOOM = 11
TEMPLATE_HTML_FILENAME = u"DwellingDigger/data/DesktopView.htm"
RESULT_HTML_FILENAME = u"DwellingDigger/DwellingMap.html"

class DesktopMainView(object):

    def show_offers(self, offers):
        points = GoogleMapPoints.from_offers(offers).as_java_script()
        FIELDS = {u"$POINTS$": points,
                  u"$MAP_CENTER_LONG$": MAP_CENTER_LONG,
                  u"$MAP_CENTER_LATT$": MAP_CENTER_LATT,
                  u"$MAP_ZOOM$" : MAP_ZOOM}
                   
        LightWebFramework.render_page_as_file(TEMPLATE_HTML_FILENAME, RESULT_HTML_FILENAME, FIELDS)  