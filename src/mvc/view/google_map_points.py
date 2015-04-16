'''
Created on 14-02-2015

@author: mateusz
'''
from _collections import defaultdict
import datetime

class GoogleMapPoints(object):
    '''
    This class converts list of dwelling offers into googlemap points string, in javascript format.
    So, just provide offers and get string, representing points ready to be displayed on a map.
    '''


    def __init__(self, points):
        """ 'points' is list of such items: [longitude, lattitude, hint, icon_name] """
        self.points = points
        
    
    @staticmethod
    def from_offers(offers):
        """ Converts list of offers into list of map points """
        
        address_to_offers_dict = GoogleMapPoints.__group_offers_by_address(offers)
        points = []
        for address, offers in address_to_offers_dict.items():
            hint = GoogleMapPoints.__prepare_hint_header(address)

            offer = None
            for offer in offers:
                address_section = offer["address_section"]
                title = offer["title"]
                date = offer["date"]
                price = offer["price"]
                url = offer["url"]
                summary = offer["summary"]
                hint = hint + GoogleMapPoints.__prepare_hint_body(title, date, price, address_section, summary, url)
                
            hint = hint.replace(u"'", u"&apos;")
            longitude, lattitude = offer["longlatt"]
            icon_name = GoogleMapPoints.__get_icon(date, len(offers))
            point = [longitude, lattitude, hint, icon_name]
            points.append(point)
        
        return GoogleMapPoints(points)       
        
    @staticmethod
    def __group_offers_by_address(offers):
        '''
        Turns list of offer into dictionary of offers grouped by address:
        offers_by_address['Wielicka 9'] = [offer1, offer2, ...]
        offers_by_address['Dworcowa 12'] = [offer1, offer2, offer3, ...]
        '''
        
        offers_by_address = defaultdict(list)
        for offer in offers:
            address = offer["address"]
            offers_by_address[address].append(offer)
            
        return offers_by_address
    
    @staticmethod
    def __prepare_hint_header(address):
        FORMATTER = u'<b>{0}</b></br>'
        return FORMATTER.format(address)

    @staticmethod
    def __prepare_hint_body(title, date, price, address_section, summary, url):
        DATE_FORMAT = "%d.%m.%Y"
        FORMATTER = u'</br><b>{2}</b>, {1}<br/>    {0}</br><i>{3}</i></br>{4}</br><a href="{5}" target="_blank">Link</a></br></hr>'
        return FORMATTER.format(title, date.strftime(DATE_FORMAT), price, address_section, summary, url)

    @staticmethod
    def __get_icon(date, num_offers):
        '''
        Returns icon name adequate for given date and number of offers aggregated.
        The icon name returned corresponds to icon name defined in *View.html template file.
        '''
        
        now = datetime.datetime.now()
        if now.year == date.year and now.month == date.month and now.day == date.day:
            # todays offers - bloody red
            return 'red_markers[%d]' % num_offers
        else:
            # older offers - light red
            return 'lightred_markers[%d]' % num_offers
        
        
    def __remove_new_lines(self, s):
        return s.replace(u'\n', u'').replace(u'\r', u'')
    
    
    def as_java_script(self):
        """ [[50.11, 10.54, 'Nowe mieszkanie w centrum...', icon_today], [...]] """
        
        string_points = []
        for point in self.points:
            s = u"[{0}, {1}, '{2}', {3}]".format(point[0], point[1], point[2], point[3])
            string_points.append(s) 
            
        js = u"[" + ", ".join(string_points) + "]"
        return self.__remove_new_lines(js)   
