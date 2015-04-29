'''
Created on 29 kwi 2015

@author: m.midor
'''
from _collections import defaultdict
import json
import datetime

class OffersGroupedByAddress(object):
    '''
    This class groups offers by their address.
    Also allows to encode the result as json string. 
    '''


    def __init__(self, groups):
        self.__groups = groups
    
    
    @classmethod
    def from_offers(cls, offers):
        ''' Factory method, constructs the instance from list of individual offers '''
        
        address_to_offers_dict = OffersGroupedByAddress.__group_offers_by_address(offers)
        groups = []
        for address, offers in address_to_offers_dict.items():
            group = OffersGroupedByAddress.__compose_offer_group(address, offers)
            groups.append(group)
            
        return cls(groups)


    @staticmethod
    def __compose_offer_group(address, offers):
        ''' Create group as a dictionary containing address, longitude, latitude and offer list '''
        
        group = {"offers":[]}
        in_offer = None
        for in_offer in offers:
            out_offer = OffersGroupedByAddress.__compose_grouped_offer(in_offer)
            group["offers"].append(out_offer)
        
        group["address"] = address
        group["longitude"], group["latitude"] = in_offer["longlatt"]
        return group
    
    
    @staticmethod
    def __compose_grouped_offer(in_offer):
        ''' Create offer as a dictionary containing selected parameters unique to an offer and not shared by whole group '''
        
        out_offer = {"title":   in_offer["title"], 
                     "date":    in_offer["date"], 
                     "price":   in_offer["price"], 
                     "url":     in_offer["url"], 
                     "image_url": in_offer["image_url"], 
                     "summary": in_offer["summary"],
                     "address_section": in_offer["address_section"]}
        return out_offer

    
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
    
    
    def get_groups(self):
        ''' Returns list of offer groups. A group collects offers with the same address '''
        return self.__groups
    
    
    def get_json_string(self):
        return json.dumps(self.__groups, default=OffersGroupedByAddress.serialize_datetime)
    
    @staticmethod
    def serialize_datetime(obj):
        ''' JSON serializer for datetime objects '''

        if isinstance(obj, datetime.datetime):
            serial = obj.strftime("%d-%m-%Y")
            return serial        