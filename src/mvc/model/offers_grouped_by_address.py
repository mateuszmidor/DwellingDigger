'''
Created on 29 kwi 2015

@author: m.midor
'''
from _collections import defaultdict
import json
import datetime
from src.mvc.view.lightwebframework.html_escape import HtmlEscape

class OffersGroupedByAddress(object):
    '''
    This class groups offers by their address, creating list of offer groups.
    Single offer group is a dictionary containing the following keys:
        ("address", "longitude", "latitude", "offers []") .
    The class allows to retrieve the created offer groups.
    It also allows to encode the offer groups as json string. 
    '''


    def __init__(self, groups):
        self.__groups = groups
    
    
    @classmethod
    def from_offers(cls, offers):
        ''' Factory method, constructs the instance from list of individual offers '''
        
        grouped_offers = OffersGroupedByAddress.__group_offers_by_address(offers)
        address_offers_groups = []
        for offers in grouped_offers:
            group = OffersGroupedByAddress.__compose_offer_group(offers)
            address_offers_groups.append(group)
            
        return cls(address_offers_groups)

    
    @staticmethod
    def __group_offers_by_address(offers):
        ''' Group offers by addres '''
        
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
        offer_with_loc_details = None
        for offer_with_loc_details in same_address_offers:
            # repack the offer not to contain location details
            offer_without_loc_details = OffersGroupedByAddress.__compact_offer(offer_with_loc_details)
            group["offers"].append(offer_without_loc_details)
        
        # assign the location details as an entry of the entire group of offers
        group["address"] = offer_with_loc_details["address"]
        group["latitude"], group["longitude"] = offer_with_loc_details["latlong"]
        return group
    
    
    @staticmethod
    def __compact_offer(in_offer):
        ''' Create offer as a dictionary containing selected parameters unique to an offer and not shared by whole group '''
        
        esc = HtmlEscape.escape
        out_offer = {"title":   esc(in_offer["title"]), 
                     "date":    in_offer["date"], 
                     "price":   in_offer["price"], 
                     "url":     in_offer["url"], 
                     "image_url":       in_offer["image_url"], 
                     "summary":         esc(in_offer["summary"]),
                     "address_section": esc(in_offer["address_section"]),
                     "num_rooms"    : in_offer["num_rooms"],
                     "area" : in_offer["area"]}
        return out_offer       
    
    
    def get_groups(self):
        ''' Returns list of offer groups. A group collects offers with the same address '''
        return self.__groups
    
    
    def get_json_string(self):
        json_string = json.dumps(self.__groups, default=OffersGroupedByAddress.serialize_datetime) 
        return json_string

    
    @staticmethod
    def serialize_datetime(obj):
        ''' JSON serializer for datetime objects '''
                
        if isinstance(obj, datetime.datetime):
            serial = obj.strftime("%d-%m-%Y")
            return serial        