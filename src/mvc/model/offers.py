'''
Created on 12-02-2015

FACADE. All needed functionality from model package you can find here
@author: mateusz
'''

from src.mvc.model.addressextractor.address_extractor import AddressExtractor
from src.mvc.model.gumtree.gumtree import Gumtree
from src.mvc.model.gumtree.offer_extractor import OfferExtractor as GumtreeOfferExtractor
from src.mvc.model.olx.offer_extractor import OfferExtractor as OlxOfferExtractor
from src.mvc.model.olx.olx import Olx
from src.outerspaceaccess.web_document_fetcher import WebDocumentFetcher
from src.multitasking.teamwork import TeamWork
from src.ioc.dependency_injector import DependencyInjector, Inject
from src.outerspaceaccess.cachinggeocoder import CachingGeocoder


@DependencyInjector("config")
class Offers(object):
    '''
    This class is facade for retrieving offers.
    Use it when you want to get actual offers matching provided OfferParams. 
    '''
    
    config = Inject
    
    @staticmethod
    def __format_full_address(street_district, city, country):
        """ Compose address string from street, city and country. street is optional """
        
        if street_district:
            return u"{0}, {1}, {2}".format(street_district, city, country)
        else:
            return u"{0}, {1}".format(city, country)
        
       
    @staticmethod 
    def __fetch_and_compose_offer(work_data):
        """
        This method unpacks offer url, offer_extrator, address_extractor, geocoder,
        downloads offer page from url and extracts offer details, then
        extracts address from offer details, finds address geolocation,
        and returns offer details along with url, address and geolocation.
        """
        
        # unpack the work data
        url, offer_extrator, address_extractor, geocoder = work_data
        
        # fetch the offer web page
        offer_page = WebDocumentFetcher.fetch(url)
        
        # parse the page and extract offer details
        offer = offer_extrator.extract(offer_page)
        
        # find address in the offer
        street_or_district = address_extractor.extract([offer["address_section"], 
                                                        offer["title"], 
                                                        offer["summary"]]) 
         
        # form nice full address string containing street, city and country
        full_address = Offers.__format_full_address(street_or_district, 
                                                    address_extractor.city, 
                                                    address_extractor.country)
        
        # add the nice address to offer details
        offer["address"] = full_address
        
        # geocode the address and add it to offer details
        latlong = geocoder.geocode(full_address)
        offer["latlong"] = latlong
        
        # add the offer page url to offer details
        offer["url"] = url 
        
        return offer
            
            
    @staticmethod
    def get_from_all_sources(offer_params, max_offer_count=5, max_parallel_count=5):
        """ 
        Gets offers from Olx and Gumtree filtered with provided criteria.
        Returned offers contain already extracted and geocoded address 
        in "address" and "longlatt" fields, respectively. 
        
        """
        
        # prepare geocoder
        cachefile = Offers.config.get("PATHS", "geocodingsCache")
        geocoder = CachingGeocoder(cachefile)
        
        # prepare address extractor for given city
        city = offer_params.get_city()
        address_extractor = AddressExtractor.for_city(city) 
        address_extractor.city = city
        address_extractor.country = "Polska"
        
        team_work = TeamWork.start_work(Offers.__fetch_and_compose_offer, max_parallel_count)
        
        for url in Gumtree.get_urls(offer_params, max_offer_count / 2):
            team_work.add_work((url, GumtreeOfferExtractor, address_extractor, geocoder))
             
        for url in Olx.get_urls(offer_params, max_offer_count / 2):
            team_work.add_work((url, OlxOfferExtractor, address_extractor, geocoder))
        
        for offer in team_work.end_work():
            yield offer