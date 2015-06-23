'''
Created on 29 kwi 2015

@author: m.midor
'''
from _collections import defaultdict
import json
import datetime
from src.mvc.view.lightwebframework.html_escape import HtmlEscape

class OffersGroupedByAddress(object):
    """
    This class groups offers by their address, creating list of offer groups.
    Single offer group is a dictionary containing the following keys:
        ("address", "longitude", "latitude", "offers []").
    """

    
    @staticmethod
    def as_json(offers):
        """ Turn individual offers into offer groups in form of a json string """
        
        groups = OffersGroupedByAddress.as_list(offers)
        json_string = json.dumps(groups, default=OffersGroupedByAddress.serialize_datetime) 
        return json_string

    
    @staticmethod
    def serialize_datetime(obj):
        """ JSON serializer for datetime objects """
                
        if isinstance(obj, datetime.datetime):
            serial = obj.strftime("%d-%m-%Y")
            return serial   
            
            
    @staticmethod
    def as_list(offers):
        """ Turn individual offers into offer groups in form of a list """
        
        offers_grouped_by_address = OffersGroupedByAddress.__group_offers_by_address(offers)
        groups = []
        for same_address_offers in offers_grouped_by_address:
            group = OffersGroupedByAddress.__compose_offer_group(same_address_offers)
            groups.append(group)
            
        return groups

    
    @staticmethod
    def __group_offers_by_address(offers):
        ''' 
        Turn individual offers into lists of offers that share same address
        eg. [[wielicka_offer1, wielicka_offer2], [dluga_offer1, dluga_offer2, dluga_offer3]]
        '''
        
        groups = defaultdict(list)
        for offer in offers:
            address = offer["address"]
            groups[address].append(offer)
            
        # we only need the grouped offers, not the addresses             
        return groups.itervalues()
    

    @staticmethod
    def __compose_offer_group(same_address_offers):
        ''' Create offer group as a dictionary containing address, longitude, latitude and offer list '''
        
        group = {"offers":[]}
        
        # original offer containing location details, ie. address and latlong (latitude, longitude tuple)
        offer = None
        for offer in same_address_offers:
            # repack the offer not to contain location details
            offer_without_loc_details = OffersGroupedByAddress.__remove_loc_details(offer)
            
            # escape the special characters in offer, so it can be presented as a part of HTML document
            html_escaped_offer = OffersGroupedByAddress.__escape_html(offer_without_loc_details)
            
            # add the processed offer to the group
            group["offers"].append(html_escaped_offer)
        
        # add the location details to the entire offer group
        group["address"] = offer["address"]
        group["latitude"], group["longitude"] = offer["latlong"]
        return group
    
    
    @staticmethod
    def __remove_loc_details(in_offer):
        ''' Create new offer that doesnt contain address, longitude nor latitude '''
        
        out_offer = {"title":   in_offer["title"], 
                     "date":    in_offer["date"], 
                     "price":   in_offer["price"], 
                     "url":     in_offer["url"], 
                     "image_url":       in_offer["image_url"], 
                     "summary":         in_offer["summary"],
                     "address_section": in_offer["address_section"],
                     "num_rooms":       in_offer["num_rooms"],
                     "area" :   in_offer["area"]}
        return out_offer       
    
    
    @staticmethod
    def __escape_html(offer):
        """ Escapes title, summary and address section for embeding in html """

        escaped_offer = dict(offer)
        escaped_offer["title"] = HtmlEscape.escape(offer["title"])
        escaped_offer["summary"] = HtmlEscape.escape(offer["summary"])
        escaped_offer["address_section"] = HtmlEscape.escape(offer["address_section"])
        return escaped_offer  
